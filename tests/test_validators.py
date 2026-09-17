from datetime import datetime
import pytest

from validators import (
    validate_date,
    validate_plate,
    validate_student_id,
    validate_employee_id,
)


class TestValidateDate:
    def test_valid_date(self):
        assert validate_date("2024-01-15") == datetime(2024, 1, 15)

    @pytest.mark.parametrize(
        "invalid_date", [
            "20X6-05-01",
            "2024/01/15",
            "15-01-2024",
            "2024-02-30",
            "",
            "   ",
        ]
    )
    def test_invalid_date(self, invalid_date):
        assert validate_date(invalid_date) is None


class TestValidatePlate:
    @pytest.mark.parametrize(
        "valid_plate", [
            "А123ВС77",
            "А200ВВ124",
            "В777АА99",
            "а123вс77",
            " Е111КХ177 ",
        ]
    )
    def test_valid_plate(self, valid_plate):
        assert validate_plate(valid_plate) is True

    @pytest.mark.parametrize(
        "invalid_plate", [
            "A123BC77",
            "Я123ВС77",
            "/000AA124",
            "А12ВС77",
            "А1234ВС77",
            "А123В77",
            "А123ВС7",
            "А123ВС7777",
            "",
            None,
        ]
    )
    def test_invalid_plate(self, invalid_plate):
        assert validate_plate(invalid_plate) is False


class TestValidateIds:
    @pytest.mark.parametrize("valid_id", ["123456", "000000", "999999"])
    def test_valid_student_id(self, valid_id):
        assert validate_student_id(valid_id) is True

    @pytest.mark.parametrize("invalid_id", ["12345", "1234567", "12345a", "", None])
    def test_invalid_student_id(self, invalid_id):
        assert validate_student_id(invalid_id) is False

    @pytest.mark.parametrize("valid_id", ["1234", "0000", "9999"])
    def test_valid_employee_id(self, valid_id):
        assert validate_employee_id(valid_id) is True

    @pytest.mark.parametrize("invalid_id", ["123", "12345", "123a", "", None])
    def test_invalid_employee_id(self, invalid_id):
        assert validate_employee_id(invalid_id) is False
