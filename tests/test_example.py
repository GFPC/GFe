from datetime import datetime
import pytest

from models import Action, StudentAction, EmployeeAction


@pytest.mark.parametrize(
    "date, plate", [
        ("20X6-05-01", "А000АА124"),
        ("20X6-05-0/", "А000АА124"),
        (datetime(2024, 5, 1), "/000AA124"),
        (datetime(2024, 5, 1), "А000БВ"),
        (datetime(2024, 5, 1), "A000AA124"),
    ]
)
def test_action_invalid_inputs(date, plate):
    with pytest.raises(ValueError):
        Action(date, plate)


def test_action_valid(valid_date, valid_plate):
    action = Action(date=valid_date, plate=valid_plate.lower())
    assert action.date == valid_date
    assert action.plate == valid_plate.upper()
    assert action.to_dict() == {
        "type": "Action",
        "date": "2024-01-15",
        "plate": valid_plate.upper(),
    }
    assert action.to_display() == f"[2024-01-15] {valid_plate.upper()}"


@pytest.mark.parametrize(
    "student_id", [
        "12345",
        "1234567",
        "12345a",
        "",
    ]
)
def test_student_action_invalid_id(valid_date, valid_plate, student_id):
    with pytest.raises(ValueError, match="error: student_id"):
        StudentAction(date=valid_date, plate=valid_plate, student_id=student_id)


def test_student_action_valid(sample_student_action):
    assert sample_student_action.student_id == "123456"
    assert sample_student_action.to_dict()["type"] == "StudentAction"
    assert "студент: 123456" in sample_student_action.to_display()


@pytest.mark.parametrize(
    "employee_id", [
        "123",
        "12345",
        "abcd",
        "",
    ]
)
def test_employee_action_invalid_id(valid_date, valid_plate, employee_id):
    with pytest.raises(ValueError, match="error: employee_id"):
        EmployeeAction(date=valid_date, plate=valid_plate, employee_id=employee_id)


def test_employee_action_valid(sample_employee_action):
    assert sample_employee_action.employee_id == "1234"
    assert sample_employee_action.department == "IT-отдел"
    assert sample_employee_action.to_dict()["type"] == "EmployeeAction"
    assert "сотрудник: 1234, отдел: IT-отдел" in sample_employee_action.to_display()
