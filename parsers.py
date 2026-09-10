"""Модуль парсинга строк и файлов с данными."""

from typing import List, Optional

from models import Action, StudentAction, EmployeeAction
from validators import validate_date


FIELD_SEPARATOR = ";"


def parse_line(line: str) -> Optional[Action]:
    """Парсит одну строку и возвращает объект Action.

    Поддерживаемые форматы:
        Action:         дата;номер
        StudentAction:  дата;номер;student_id
        EmployeeAction: дата;номер;employee_id;отдел

    Args:
        line: Строка с данными.

    Returns:
        Объект Action или None, если строка некорректна.
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    parts = [p.strip() for p in line.split(FIELD_SEPARATOR)]

    try:
        if len(parts) == 2:
            date = validate_date(parts[0])
            if date is None:
                return None
            return Action(date=date, plate=parts[1])

        elif len(parts) == 3:
            date = validate_date(parts[0])
            if date is None:
                return None
            return StudentAction(
                date=date,
                plate=parts[1],
                student_id=parts[2],
            )

        elif len(parts) == 4:
            date = validate_date(parts[0])
            if date is None:
                return None
            return EmployeeAction(
                date=date,
                plate=parts[1],
                employee_id=parts[2],
                department=parts[3],
            )

        else:
            return None

    except ValueError:
        return None


def parse_file(filepath: str) -> List[Action]:
    """Парсит файл с данными.

    Args:
        filepath: Путь к файлу.

    Returns:
        Список объектов Action.
    """
    actions = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                action = parse_line(line)
                if action is not None:
                    actions.append(action)
    except FileNotFoundError:
        print(f"error: file not found: {filepath}")
    except IOError as e:
        print(f"error: cannot read file: {e}")
    return actions


def parse_string(text: str) -> List[Action]:
    """Парсит многострочную строку с данными.

    Args:
        text: Строка с данными (разделитель  перенос строки).

    Returns:
        Список объектов Action.
    """
    actions = []
    for line in text.splitlines():
        action = parse_line(line)
        if action is not None:
            actions.append(action)
    return actions
