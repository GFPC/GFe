from datetime import datetime
import pytest

from models import Action, StudentAction, EmployeeAction
from storage import InMemoryDB


@pytest.fixture
def valid_date():
    return datetime(2024, 1, 15)


@pytest.fixture
def valid_plate():
    return "А123ВС77"


@pytest.fixture
def sample_action(valid_date, valid_plate):
    return Action(date=valid_date, plate=valid_plate)


@pytest.fixture
def sample_student_action(valid_date, valid_plate):
    return StudentAction(date=valid_date, plate=valid_plate, student_id="123456")


@pytest.fixture
def sample_employee_action(valid_date, valid_plate):
    return EmployeeAction(date=valid_date, plate=valid_plate, employee_id="1234", department="IT-отдел")


@pytest.fixture
def db():
    return InMemoryDB()
