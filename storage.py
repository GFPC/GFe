"""Модуль хранения данных (InMemoryDB)."""

from typing import List, Dict, Any

from models import Action


class InMemoryDB:
    """Простое in-memory хранилище объектов Action.

    Attributes:
        _records: Внутренний список записей.
    """

    def __init__(self) -> None:
        self._records: List[Dict[str, Any]] = []

    def add(self, action: Action) -> None:
        """Добавляет объект в хранилище.

        Args:
            action: Объект Action для добавления.
        """
        self._records.append(action.to_dict())

    def add_many(self, actions: List[Action]) -> None:
        """Добавляет несколько объектов.

        Args:
            actions: Список объектов Action.
        """
        for action in actions:
            self.add(action)

    def get_all(self) -> List[Dict[str, Any]]:
        """Возвращает все записи."""
        return list(self._records)

    def clear(self) -> None:
        """Очищает хранилище."""
        self._records.clear()

    def count(self) -> int:
        """Возвращает количество записей."""
        return len(self._records)

    def find_by_plate(self, plate: str) -> List[Dict[str, Any]]:
        """Ищет записи по номеру автомобиля.

        Args:
            plate: Номер автомобиля.

        Returns:
            Список найденных записей.
        """
        plate = plate.upper().strip()
        return [r for r in self._records if r.get("plate") == plate]

    def print_all(self) -> None:
        """Выводит все записи в консоль."""
        if not self._records:
            print("DB is empty")
            return
        for record in self._records:
            print(record)
