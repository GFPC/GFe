"""Главный модуль программы.

Демонстрирует:
- Работу с одиночным объектом
- Обработку набора объектов из строки
- Обработку набора объектов из файла
"""

import sys

from models import Action
from parsers import parse_string, parse_file
from storage import InMemoryDB
from validators import validate_date


def process_single_action() -> Action | None:
    """Обрабатывает один объект, введенный пользователем."""
    date_input = input("Введите дату (YYYY-MM-DD): ").strip()
    plate_input = input("Введите номер автомобиля: ").strip()

    date = validate_date(date_input)
    if date is None:
        print("error: date")
        return None

    try:
        action = Action(date=date, plate=plate_input)
        action.print()
        return action
    except ValueError as e:
        print(e)
        return None


def process_string_example() -> list:
    """Демонстрирует обработку набора объектов из строки."""
    sample = """\
2024-01-15;А123ВС77
2024-01-16;В456ЕК99;123456
2024-01-17;С789МН50;1234;IT-отдел
2024-01-18;О321РТ77;654321
"""
    print("\n=== Обработка набора из строки ===")
    actions = parse_string(sample)
    for action in actions:
        action.print()
    return actions


def process_file_example(filepath: str) -> list:
    """Демонстрирует обработку набора объектов из файла.

    Args:
        filepath: Путь к файлу с данными.
    """
    print(f"\n=== Обработка файла: {filepath} ===")
    actions = parse_file(filepath)
    if not actions:
        print("Нет данных для обработки")
        return []
    for action in actions:
        action.print()
    return actions


def main() -> None:
    """Точка входа в программу."""
    db = InMemoryDB()

    single = process_single_action()
    if single is not None:
        db.add(single)

    string_actions = process_string_example()
    db.add_many(string_actions)

    filepath = sys.argv[1] if len(sys.argv) > 1 else "data/actions.txt"
    file_actions = process_file_example(filepath)
    db.add_many(file_actions)

    print("\n=== Итоговое хранилище ===")
    print(f"Всего записей: {db.count()}")
    db.print_all()


if __name__ == "__main__":
    main()
