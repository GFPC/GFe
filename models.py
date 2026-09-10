"""Модуль с классами объектов учета проезда.

Каждый класс отвечает за один тип объекта:
- Action: базовый проезд автомобиля
- StudentAction: проезд студента (с номером студенческого)
- EmployeeAction: проезд сотрудника (с табельным номером)
"""

from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Any

from validators import (
    validate_plate,
    validate_student_id,
    validate_employee_id,
)


@dataclass
class Action:
    """Базовый объект  проезд автомобиля.

    Attributes:
        date: Дата проезда.
        plate: Номер автомобиля.
    """
    date: datetime
    plate: str

    def __post_init__(self):
        """Валидация после инициализации."""
        if not isinstance(self.date, datetime):
            raise ValueError("error: date")
        if not validate_plate(self.plate):
            raise ValueError("error: plate")
        self.plate = self.plate.upper().strip()

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект в словарь для хранения."""
        return {
            "type": "Action",
            "date": self.date.strftime("%Y-%m-%d"),
            "plate": self.plate,
        }

    def to_display(self) -> str:
        """Формирует строку для вывода."""
        return f"[{self.date.strftime('%Y-%m-%d')}] {self.plate}"

    def print(self) -> None:
        """Выводит объект в консоль."""
        print(self.to_display())


@dataclass
class StudentAction(Action):
    """Проезд студента  расширяет Action номером студенческого.

    Attributes:
        student_id: Номер студенческого билета (6 цифр).
    """
    student_id: str = ""

    def __post_init__(self):
        super().__post_init__()
        if not validate_student_id(self.student_id):
            raise ValueError("error: student_id")

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект в словарь."""
        data = super().to_dict()
        data["type"] = "StudentAction"
        data["student_id"] = self.student_id
        return data

    def to_display(self) -> str:
        """Формирует строку для вывода."""
        base = super().to_display()
        return f"{base} [студент: {self.student_id}]"


@dataclass
class EmployeeAction(Action):
    """Проезд сотрудника  расширяет Action табельным номером.

    Attributes:
        employee_id: Табельный номер сотрудника (4 цифры).
        department: Название отдела (опционально).
    """
    employee_id: str = ""
    department: str = ""

    def __post_init__(self):
        super().__post_init__()
        if not validate_employee_id(self.employee_id):
            raise ValueError("error: employee_id")

    def to_dict(self) -> Dict[str, Any]:
        """Преобразует объект в словарь."""
        data = super().to_dict()
        data["type"] = "EmployeeAction"
        data["employee_id"] = self.employee_id
        data["department"] = self.department
        return data

    def to_display(self) -> str:
        """Формирует строку для вывода."""
        base = super().to_display()
        dept = f", отдел: {self.department}" if self.department else ""
        return f"{base} [сотрудник: {self.employee_id}{dept}]"
