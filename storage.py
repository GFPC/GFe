from typing import List, Dict, Any

from models import Action


class InMemoryDB:
    def __init__(self) -> None:
        self._records: List[Dict[str, Any]] = []

    def add(self, action: Action) -> None:
        self._records.append(action.to_dict())

    def add_many(self, actions: List[Action]) -> None:
        for action in actions:
            self.add(action)

    def get_all(self) -> List[Dict[str, Any]]:
        return list(self._records)

    def clear(self) -> None:
        self._records.clear()

    def count(self) -> int:
        return len(self._records)

    def find_by_plate(self, plate: str) -> List[Dict[str, Any]]:
        plate = plate.upper().strip()
        return [r for r in self._records if r.get("plate") == plate]

    def print_all(self) -> None:
        if not self._records:
            print("DB is empty")
            return
        for record in self._records:
            print(record)