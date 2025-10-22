# core/table.py
from abstracts import Table_
from typing import Any
import uuid


class Table(Table_):
    """Concrete table representation with schema and data."""

    def __init__(self, name: str = "", table_id: str | None = None):
        super().__init__(name)
        self.table_id = table_id or str(uuid.uuid4())
        self.parameters: dict[str, Any] = {"name": name}
        self.fields: list[str] = []
        self.values: list[list[Any]] = []

    def from_json(self, data: dict[str, Any]) -> None:
        self.table_id = data.get("table_id", str(uuid.uuid4()))
        self.parameters = data.get("parameters", {})
        self.fields = data.get("fields", [])
        self.values = data.get("values", [])
        self.name = self.parameters.get("name", self.name)

    def to_json(self) -> dict[str, Any]:
        return {
            "table_id": self.table_id,
            "parameters": self.parameters,
            "fields": self.fields,
            "values": self.values,
        }

    def insert(self, record: list[Any]) -> None:
        if len(record) != len(self.fields):
            raise ValueError("Record length does not match number of fields")
        self.values.append(record)

    def all(self) -> list[list[Any]]:
        return self.values
