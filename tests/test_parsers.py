from datetime import datetime
from parsers import parse_line, parse_string, parse_file
from models import Action, StudentAction, EmployeeAction


class TestParseLine:
    def test_empty_and_comment_lines(self):
        assert parse_line("") is None
        assert parse_line("   ") is None
        assert parse_line("# comment") is None

    def test_parse_action(self):
        line = "2024-01-15;А123ВС77"
        action = parse_line(line)
        assert isinstance(action, Action)
        assert not isinstance(action, (StudentAction, EmployeeAction))
        assert action.date == datetime(2024, 1, 15)
        assert action.plate == "А123ВС77"

    def test_parse_student_action(self):
        line = "2024-01-16;В456ЕК99;123456"
        action = parse_line(line)
        assert isinstance(action, StudentAction)
        assert action.student_id == "123456"

    def test_parse_employee_action(self):
        line = "2024-01-17;С789МН50;1234;IT-отдел"
        action = parse_line(line)
        assert isinstance(action, EmployeeAction)
        assert action.employee_id == "1234"
        assert action.department == "IT-отдел"

    def test_parse_invalid_line(self):
        assert parse_line("invalid line") is None
        assert parse_line("2024-01-15;А123ВС77;12;IT;extra") is None
        assert parse_line("2024-01-15;INVALID") is None
        assert parse_line("INVALID;А123ВС77") is None


class TestParseStringAndFile:
    def test_parse_string(self):
        text = """# comment
2024-01-15;А123ВС77
2024-01-16;В456ЕК99;123456
invalid
2024-01-17;С789МН50;1234;IT-отдел
"""
        actions = parse_string(text)
        assert len(actions) == 3
        assert isinstance(actions[0], Action)
        assert isinstance(actions[1], StudentAction)
        assert isinstance(actions[2], EmployeeAction)

    def test_parse_file(self, tmp_path):
        test_file = tmp_path / "test_actions.txt"
        test_file.write_text("2024-01-15;А123ВС77\n2024-01-16;В456ЕК99;123456\n", encoding="utf-8")

        actions = parse_file(str(test_file))
        assert len(actions) == 2

    def test_parse_file_not_found(self):
        actions = parse_file("non_existent_file_path.txt")
        assert actions == []
