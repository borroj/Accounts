from abc import ABC, abstractmethod
from typing import Any


class Database_(ABC):
    """Abstract base class for simple persistent databases."""

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def load(self) -> None:
        """Load database contents from disk."""
        pass

    @abstractmethod
    def save(self) -> None:
        """Save database contents to disk."""
        pass

    @abstractmethod
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value by key, or return a default if not found."""
        pass

    @abstractmethod
    def set(self, key: str, value: Any) -> None:
        """Set a key-value pair."""
        pass

    @abstractmethod
    def delete(self, key: str) -> None:
        """Remove a key-value pair."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear all entries in the database."""
        pass

    def __getitem__(self, key: str) -> Any:
        return self.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.set(key, value)

    def __delitem__(self, key: str) -> None:
        self.delete(key)

    def __contains__(self, key: str) -> bool:
        return self.get(key) is not None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(path='{self.path}')"



class Table_(ABC):
    """Abstract representation of a database table."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def from_json(self, data: Any) -> None:
        """Populate table from a JSON structure."""
        pass

    @abstractmethod
    def to_json(self) -> Any:
        """Return table content as JSON-serializable structure."""
        pass

    @abstractmethod
    def insert(self, record: dict[str, Any]) -> None:
        """Insert a record into the table."""
        pass

    @abstractmethod
    def all(self) -> list[dict[str, Any]]:
        """Return all records."""
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}')"
