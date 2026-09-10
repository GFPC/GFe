"""Модуль валидации входных данных."""

import re
from datetime import datetime
from typing import Optional


PLATE_PATTERN = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
DATE_FORMAT = "%Y-%m-%d"


def validate_date(date_str: str) -> Optional[datetime]:
    """Проверяет корректность даты и возвращает datetime.

    Args:
        date_str: Строка с датой в формате YYYY-MM-DD.

    Returns:
        datetime, если дата корректна, иначе None.
    """
    try:
        return datetime.strptime(date_str.strip(), DATE_FORMAT)
    except (ValueError, AttributeError):
        return None


def validate_plate(plate: str) -> bool:
    """Проверяет формат автомобильного номера РФ.

    Args:
        plate: Строка с номером автомобиля.

    Returns:
        True, если номер соответствует формату, иначе False.
    """
    if not plate or not isinstance(plate, str):
        return False
    return bool(PLATE_PATTERN.match(plate.strip().upper()))


def validate_student_id(student_id: str) -> bool:
    """Проверяет формат номера студенческого билета.

    Формат: 6 цифр (например, 123456).

    Args:
        student_id: Строка с номером студенческого.

    Returns:
        True, если номер корректен, иначе False.
    """
    if not student_id or not isinstance(student_id, str):
        return False
    return bool(re.match(r'^\d{6}$', student_id.strip()))


def validate_employee_id(employee_id: str) -> bool:
    """Проверяет формат табельного номера сотрудника.

    Формат: 4 цифры (например, 1234).

    Args:
        employee_id: Строка с табельным номером.

    Returns:
        True, если номер корректен, иначе False.
    """
    if not employee_id or not isinstance(employee_id, str):
        return False
    return bool(re.match(r'^\d{4}$', employee_id.strip()))
