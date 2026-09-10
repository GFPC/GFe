import re
from datetime import datetime
from typing import Optional


PLATE_PATTERN = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$')
STUDENT_ID_PATTERN = re.compile(r'^\d{6}$')
EMPLOYEE_ID_PATTERN = re.compile(r'^\d{4}$')
DATE_FORMAT = "%Y-%m-%d"


def validate_date(date_str: str) -> Optional[datetime]:
    try:
        return datetime.strptime(date_str.strip(), DATE_FORMAT)
    except (ValueError, AttributeError):
        return None


def validate_plate(plate: str) -> bool:
    if not plate or not isinstance(plate, str):
        return False
    return bool(PLATE_PATTERN.match(plate.strip().upper()))


def validate_student_id(student_id: str) -> bool:
    if not student_id or not isinstance(student_id, str):
        return False
    return bool(STUDENT_ID_PATTERN.match(student_id.strip()))


def validate_employee_id(employee_id: str) -> bool:
    if not employee_id or not isinstance(employee_id, str):
        return False
    return bool(EMPLOYEE_ID_PATTERN.match(employee_id.strip()))