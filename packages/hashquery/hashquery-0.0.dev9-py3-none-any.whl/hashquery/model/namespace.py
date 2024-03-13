from typing import *

from .column_expression.column_expression import ColumnExpression
from ..utils.identifiable import Identifiable
from ..utils.serializable import Serializable

if TYPE_CHECKING:
    from .model import Model


class ModelNamespace(Serializable, Identifiable):
    """
    Represents a namespace within a Model, typically through a JOIN,
    though we also create virtual namespaces for some APIs to scope a
    collection of properties together.

    A virtual namespace will not apply `.disambiguated` on column access
    against it. It effectively acts as a proxy to access inner attributes
    and nested namespaces, and this namespace only exists within Python,
    not within the final SQL.
    """

    def __init__(
        self,
        identifier: str,
        nested_model: "Model",
        is_virtual: bool = False,
    ) -> None:
        self.identifier = identifier
        self.nested_model = nested_model
        self.is_virtual = is_virtual

    # proxy accessing attributes, disambiguating with self
    def __getattr__(self, name: str) -> Any:
        # use standard lookup for these keys, else this could result
        # in an infinite loop (since this function references them)
        if name.startswith("__") or name in ["identifier", "nested_model"]:
            raise AttributeError()

        nested_result = getattr(self.nested_model, name)
        if isinstance(nested_result, ColumnExpression) and not self.is_virtual:
            return nested_result.disambiguated(self)
        return nested_result

    # --- Serialization ---

    def to_wire_format(self) -> Dict:
        return {
            "type": "modelNamespace",
            "identifier": self.identifier,
            "nestedModel": self.nested_model.to_wire_format(),
            "isVirtual": self.is_virtual,
        }

    @classmethod
    def from_wire_format(cls, wire: Dict) -> "ModelNamespace":
        from .model import Model  # need the actual implementation

        assert wire["type"] == "modelNamespace"
        return ModelNamespace(
            identifier=wire["identifier"],
            nested_model=Model.from_wire_format(wire["nestedModel"]),
            is_virtual=wire["isVirtual"],
        )
