from typing import *
from copy import deepcopy

from ..utils.access_proxy import AccessProxy
from ..utils.builder import builder_method
from ..utils.serializable import Serializable
from ..utils.keypath import (
    _,
    resolve_keypath_args_from,
    resolve_keypath,
    unwrap_keypath_to_name,
    KeyPath,
)
from ..utils.identifiable import (
    Identifiable,
    IdentifiableMap,
)
from ..utils.resource import LinkedResource
from .column_expression import (
    ColumnExpression,
    SqlTextColumnExpression,
    ColumnNameColumnExpression,
)
from .column_expression.cases import cases
from .column_expression.sql_function import count, count_if
from .source import (
    Source,
    SqlTextSource,
    AggregateSource,
    FilterSource,
    PickSource,
    SortSource,
    LimitSource,
    JoinOneSource,
    MatchStepsSource,
)
from .namespace import ModelNamespace
from .activity_schema import ModelActivitySchema


class Model(Serializable, Identifiable):
    def __init__(self) -> None:
        self.connection: LinkedResource = None
        self.source: Source = None
        self.attributes = IdentifiableMap[ColumnExpression]()
        self.measures = IdentifiableMap[ColumnExpression]()
        self.namespaces = IdentifiableMap[ModelNamespace]()
        self.primary_key: ColumnExpression = ColumnNameColumnExpression("id")
        self.activity_schema: Optional[ModelActivitySchema] = None
        self.custom_meta = {}
        # internally used to understand the origin of a model
        # and its relation to an original Hashboard resource
        self.linked_resource: Optional[LinkedResource] = None

    # allow accessing nested properties via direct `.` access
    # instead of always going through `model.attributes.` or similar
    def __getattr__(self, name: str) -> Any:
        # use standard lookup for these keys, else this could result
        # in an infinite loop (since this function references them)
        if name.startswith("__") or name in ["attributes", "measures", "namespaces"]:
            raise AttributeError()

        maps: List[IdentifiableMap] = [self.attributes, self.measures, self.namespaces]
        matches = [i for i in [map.get(name) for map in maps] if i is not None]
        # TODO: if we don't find anything here, and our source is a SQL thing,
        # we should just assume there's an attribute with that name, and
        # optimistically return a ColumnExpression with `column(name)`.
        # That way you don't need to define all the physical columns of your
        # model in order to reference them.
        matched_count = len(matches)
        if matched_count == 1:
            return matches[0]
        if matched_count == 0:
            raise AttributeError(
                f"Model has no attribute, measure, or namespace with name '{name}'"
            )
        else:
            raise AttributeError(
                f"'{name}' is ambiguous on model. "
                + f"{matched_count} attributes, measures, or namespaces share that name. "
                + "Rename one of the properties with `named`."
            )

    # --- Adding Properties ---

    @builder_method
    def with_data_source(
        self,
        connection: LinkedResource,
        source: Union[Source, SqlTextColumnExpression],
    ) -> "Model":
        """
        Forms a new Model with the provided data source as the underlying table.
        If the receiver already had a source attached, this overwrites that
        reference, including any transformations to that source.

        If you want to join or union multiple datasets, use
        `Model.with_join_one` or `Model.union`.
        """
        self.connection = connection
        if type(source) is SqlTextColumnExpression:
            # We accept `SqlTextColumnExpression` here and convert it to a
            # `SqlTextSource`. This is because the free function
            # `sql("...")` would be a reasonable thing to pass into
            # this, and that returns a `ColumnExpression`.
            # If only we had contextual typing! I miss Swift...      :'(
            source = SqlTextSource(source.sql)
        self.source = source

    @builder_method
    @resolve_keypath_args_from(_.self)
    def with_attribute(self, expression: Union[ColumnExpression, str]) -> "Model":
        """
        Forms a new Model with the provided column expression included as an
        attribute. If a string is passed, this will interpret it as a column
        name if it is a valid identifier, else as literal SQL.
        """
        if type(expression) == str:
            expression = (
                ColumnNameColumnExpression(expression)
                if expression.isidentifier()
                else SqlTextColumnExpression(expression)
            )
        self.attributes.add(expression)

    @builder_method
    @resolve_keypath_args_from(_.self)
    def with_primary_key(self, expression: Union[ColumnExpression, str]) -> "Model":
        """
        Forms a new model with the provided column expression configured as the
        primary key. This should be a unique value across all records in the
        source. By default, this is `column("id")`.
        """
        if type(expression) == str:
            expression = (
                ColumnNameColumnExpression(expression)
                if expression.isidentifier()
                else SqlTextColumnExpression(expression)
            )
        self.primary_key = expression

    @builder_method
    @resolve_keypath_args_from(_.self)
    def with_measure(self, expression: ColumnExpression) -> "Model":
        """
        Forms a new Model with the provided column expression included as a
        measure definition. This does not perform any aggregation on its own,
        this just attaches a definition for later use.
        """
        self.measures.add(expression)

    @builder_method
    def with_join_one(
        self,
        joined: "Model",
        *,
        on: Optional[Union[ColumnExpression, KeyPath]] = None,
        condition: Callable[
            ["ModelAttributes", "ModelAttributes"],
            ColumnExpression,
        ] = None,
        named: Optional[Union[str, KeyPath]] = None,
        drop_unmatched: bool = False,
    ) -> "Model":
        """
        Forms a new Model with a new property which can be used to reference
        the properties of the `joined` Model. Records are aligned using `condition`.

        Similar to `with_measure` and `with_attribute`, `with_join_one` has no
        performance cost on its own. No JOIN statement is added to queries
        unless the relation is actually referenced.

        This never changes the record count of the data by exploding rows.
        If multiple records match, only the first matching record is joined.
        If you want to explode records, use `Model.cross_join` instead.

        If no records match, `NULL` values are filled in for the missing columns,
        unless `drop_unmatched=True` is passed.
        """
        # -- gather all the parameters up, resolve and validate --
        if on is None and condition is None:
            raise ValueError(
                "`.with_join_one` must specify a join condition using "
                + "`on=<foreign_key>` and/or `condition=<column_expression>`"
            )
        if type(joined) == KeyPath:
            joined = resolve_keypath(self, joined)
        relation_name = unwrap_keypath_to_name(named)
        if not relation_name:
            if default_identifier := joined.source._default_identifier():
                relation_name = default_identifier
        if not relation_name:
            raise ValueError(
                "Join was not provided an identifier and a default could not be inferred. "
                + "Provide an explicit name for this relation using `named=`"
            )

        # -- determine the column expression to join with --
        join_predicate = None
        if on is not None:
            on: ColumnExpression = (
                resolve_keypath(self, on) if (type(on) == KeyPath) else on
            )
            join_predicate = on == joined.primary_key.disambiguated(relation_name)
        if condition is not None:
            condition_predicate = condition(
                # within the condition expression, only attributes can be
                # accessed, and disambiguate the right-side
                AccessProxy(self.attributes),
                AccessProxy(
                    joined.attributes,
                    lambda c: c.disambiguated(relation_name),
                ),
            )
            join_predicate = (
                condition_predicate
                if not join_predicate
                else join_predicate & condition_predicate
            )

        # -- attach the final relation --
        relation = ModelNamespace(identifier=relation_name, nested_model=joined)
        self.source = JoinOneSource(
            base=self.source,
            relation=relation,
            join_condition=join_predicate,
            drop_unmatched=drop_unmatched,
        )
        self.namespaces.add(relation)

    @builder_method
    @resolve_keypath_args_from(_.self)
    def with_activity_schema(
        self,
        *,
        group: ColumnExpression,
        axis: ColumnExpression,
        event_key: ColumnExpression,
    ) -> "Model":
        """
        Returns a new Model configured for event analysis.

        Args:
            group:
                Used to split event sequences into distinct groups.
                Typically this is a single attribute, representing
                a unique value for each actor that invokes the event,
                such as `user_id` or `customer_id`.

            axis:
                A timestamp/numeric used to order events occurred.
                Typically this is a timestamp representing when the event
                was detected, such as `created_at` or `timestamp`.

            event_key:
                A column representing the name of the event.
                Typically this is a column like `event_name` or `event_type`.
        """
        self.activity_schema = ModelActivitySchema(
            group=group,
            axis=axis,
            event_key=event_key,
        )

    @builder_method
    @resolve_keypath_args_from(_.self)
    def with_custom_meta(self, name: str, value: Any) -> "Model":
        """
        Forms a new Model with the custom metadata attached on `.custom_meta[name]`.
        Hashboard will never read or write to the `custom_meta` dictionary, making
        it a good spot to put any custom configuration or encode semantic information
        about the Model you can use later.
        """
        self.custom_meta[name] = value

    # --- Analysis ---

    @builder_method
    @resolve_keypath_args_from(_.self)
    def aggregate(
        self,
        *,
        groups: List[ColumnExpression] = None,
        measures: List[ColumnExpression] = None,
    ) -> "Model":
        """
        Returns a new model aggregated into `measures` split up by `groups`.
        Analogous to `SELECT *groups, *measures FROM ... GROUP BY *groups`.
        """
        groups = groups or []
        measures = measures or []
        self.source = AggregateSource(self.source, groups=groups, measures=measures)
        self.attributes = IdentifiableMap(
            ColumnNameColumnExpression(c.identifier) for c in groups + measures
        )
        self.measures = IdentifiableMap()
        self.namespaces = IdentifiableMap()

    @builder_method
    @resolve_keypath_args_from(_.self)
    def match_steps(
        self,
        *steps: List[str],
        group: Optional[ColumnExpression] = None,
        axis: Optional[ColumnExpression] = None,
        event_key: Optional[ColumnExpression] = None,
    ) -> "Model":
        """
        Returns a new source with a new property that represents the records
        matched to a sequence of steps, aggregated by `group`.

        Useful for defining funnels, retention, or temporal joins.
        """
        # `self` pre-transformation is the events table we'll use as a base
        events_model = deepcopy(self)

        # normalize the activity schema, defaulting to what was modeled
        activity_schema = (
            ModelActivitySchema(group=group, axis=axis, event_key=event_key)
            if (group and axis and event_key)
            else self.activity_schema
        )
        if not activity_schema:
            raise ValueError(
                "`match_steps` requires the model to have an activity schema defined. "
                + "Use `.with_activity_schema` to define the schema upstream, "
                + "or fully qualify `group`, `axis` and `event_key` in the call to `match_steps`"
            )

        # attach the source transform to build and attach step event data
        self.source = MatchStepsSource(
            base=self.source,
            activity_schema=activity_schema,
            steps=steps,
        )

        # add a new namespace for each step containing the attributes
        # on the events table, which the `MatchStepsSource` will generate
        self.namespaces = IdentifiableMap[ModelNamespace]()
        for step in steps:  # self join on each step's name
            self.namespaces.add(ModelNamespace(step, events_model))

        # reset the attributes to only what will be available after transform
        self.attributes = IdentifiableMap([activity_schema.group])
        self.attributes.add(
            # helper to get the last matched step
            cases(
                *[
                    (
                        activity_schema.event_key.disambiguated(step) != None,
                        step,
                    )
                    for step in reversed(steps)
                ],
                other=None,
            ).named("last_matched_step_name")
        )
        self.primary_key = activity_schema.group  # best effort

        # reset the measures
        self.measures = IdentifiableMap()
        self.measures.add(count())
        for step in steps:
            # helper to get the count of records which reached the step
            self.measures.add(
                count_if(activity_schema.event_key.disambiguated(step) != None).named(
                    f"{step}_count"
                )
            )

        # the existing activity schema's properties have been consumed
        # and are no longer valid
        self.activity_schema = None

    # --- Record Management ---

    @builder_method
    @resolve_keypath_args_from(_.self)
    def pick(self, columns: List[ColumnExpression]) -> "Model":
        """
        Forms a new Model with only the included attributes included.
        """
        self.source = PickSource(self.source, columns)
        self.attributes = IdentifiableMap(
            ColumnNameColumnExpression(c.identifier) for c in columns
        )
        self.namespaces = IdentifiableMap()
        # we might want to preserve measures if we can inspect them
        # and confirm they only rely on selected columns (?)
        self.measures = IdentifiableMap()

    @builder_method
    @resolve_keypath_args_from(_.self)
    def filter(self, condition: ColumnExpression) -> "Model":
        """
        Forms a new Model with records filtered to only those which
        match the given condition.
        """
        self.source = FilterSource(self.source, condition)

    @builder_method
    @resolve_keypath_args_from(_.self)
    def sort(self, sort: ColumnExpression) -> "Model":
        """
        Forms a new Model with records ordered by the provided column.
        """
        self.source = SortSource(self.source, sort)

    @builder_method
    @resolve_keypath_args_from(_.self)
    def take(self, count: int) -> "Model":
        """
        Forms a new Model with only the first N records.
        """
        self.source = LimitSource(self.source, count)

    # --- Serialization ---

    def to_wire_format(self) -> dict:
        return {
            "type": "model",
            "connection": self.connection.to_wire_format(),
            "source": self.source.to_wire_format(),
            "attributes": [a.to_wire_format() for a in self.attributes],
            "measures": [m.to_wire_format() for m in self.measures],
            "namespaces": [n.to_wire_format() for n in self.namespaces],
            "primaryKey": self.primary_key.to_wire_format(),
            "activitySchema": (
                self.activity_schema.to_wire_format() if self.activity_schema else None
            ),
            "customMeta": self.custom_meta,
            "linkedResource": (
                self.linked_resource.to_wire_format() if self.linked_resource else None
            ),
        }

    @classmethod
    def from_wire_format(cls, wire: dict):
        assert wire["type"] == "model"
        result = Model()
        result.connection = LinkedResource.from_wire_format(wire["connection"])
        result.source = Source.from_wire_format(wire["source"])
        result.attributes = IdentifiableMap(
            ColumnExpression.from_wire_format(a) for a in wire.get("attributes", [])
        )
        result.measures = IdentifiableMap(
            ColumnExpression.from_wire_format(m) for m in wire.get("measures", [])
        )
        result.namespaces = IdentifiableMap(
            ModelNamespace.from_wire_format(n) for n in wire.get("namespaces", [])
        )
        result.primary_key = ColumnExpression.from_wire_format(wire["primaryKey"])
        result.activity_schema = (
            ModelActivitySchema.from_wire_format(wire["activitySchema"])
            if wire.get("activitySchema")
            else None
        )
        result.custom_meta = wire.get("customMeta", {})
        result.linked_resource = (
            LinkedResource.from_wire_format(wire["linkedResource"])
            if wire["linkedResource"]
            else None
        )
        return result


ModelAttributes = AccessProxy["Model", ColumnExpression]
