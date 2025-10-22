# core/database.py
import json
from abstracts import Database_
from table import Table


class Database(Database_):
    """Concrete JSON database where root is a list of tables."""

    def __init__(self, path: str):
        super().__init__(path)
        self.load()

    def from_json(self, data: list[dict]) -> None:
        self.tables.clear()

        for tdata in data:
            table = Table()
            table.from_json(tdata)
            self.add_table(table)

        # optional global info
        self.parameters["table_count"] = len(self.tables)

    def to_json(self) -> list[dict]:
        return [t.to_json() for t in self.tables.values()]

    def load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.from_json(data)
                else:
                    raise ValueError("Invalid JSON format: expected list at root")
        except FileNotFoundError:
            self.tables = {}
            self.parameters = {}

    def save(self) -> None:
        data = self.to_json()
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
