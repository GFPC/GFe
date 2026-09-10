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
    date: datetime
    plate: str

    def __post_init__(self):
        if not isinstance(self.date, datetime):
            raise ValueError("error: date")
        if not validate_plate(self.plate):
            raise ValueError("error: plate")
        self.plate = self.plate.upper().strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "Action",
            "date": self.date.strftime("%Y-%m-%d"),
            "plate": self.plate,
        }

    def to_display(self) -> str:
        return f"[{self.date.strftime('%Y-%m-%d')}] {self.plate}"

    def print(self) -> None:
        print(self.to_display())


@dataclass
class StudentAction(Action):
    student_id: str = ""

    def __post_init__(self):
        super().__post_init__()
        if not validate_student_id(self.student_id):
            raise ValueError("error: student_id")

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["type"] = "StudentAction"
        data["student_id"] = self.student_id
        return data

    def to_display(self) -> str:
        base = super().to_display()
        return f"{base} [студент: {self.student_id}]"


@dataclass
class EmployeeAction(Action):
    employee_id: str = ""
    department: str = ""

    def __post_init__(self):
        super().__post_init__()
        if not validate_employee_id(self.employee_id):
            raise ValueError("error: employee_id")

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["type"] = "EmployeeAction"
        data["employee_id"] = self.employee_id
        data["department"] = self.department
        return data

    def to_display(self) -> str:
        base = super().to_display()
        dept = f", отдел: {self.department}" if self.department else ""
        return f"{base} [сотрудник: {self.employee_id}{dept}]"
