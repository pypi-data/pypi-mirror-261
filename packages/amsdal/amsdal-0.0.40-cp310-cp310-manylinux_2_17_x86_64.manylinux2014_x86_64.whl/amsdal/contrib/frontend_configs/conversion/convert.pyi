from _typeshed import Incomplete
from amsdal.schemas.manager import SchemaManager as SchemaManager
from types import UnionType
from typing import Any

default_types_map: Incomplete

def _process_union(value: UnionType) -> dict[str, Any]: ...
def convert_to_frontend_config(value: Any) -> dict[str, Any]: ...
