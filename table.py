# core/table.py
from abstracts import Table_


class Table(Table_):
    """Simple in-memory table based on list of dicts."""

    def __init__(self, name: str):
        super().__init__(name)
        self.rows: list[dict] = []

    def from_json(self, data):
        self.rows = data if isinstance(data, list) else []

    def to_json(self):
        return self.rows

    def insert(self, record: dict):
        self.rows.append(record)

    def all(self):
        return self.rows
