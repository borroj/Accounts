import json
from typing import Any
from abstracts import Database_


class Database(Database_):
    def __init__(self, path: str):
        super().__init__(path)
        self.data: dict[str, Any] = {}
        self.load()

    def load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.data[key] = value
        self.save()

    def delete(self, key: str) -> None:
        if key in self.data:
            del self.data[key]
            self.save()

    def clear(self) -> None:
        self.data.clear()
        self.save()
