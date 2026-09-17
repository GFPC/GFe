def test_db_add_and_count(db, sample_action):
    assert db.count() == 0
    db.add(sample_action)
    assert db.count() == 1
    assert len(db.get_all()) == 1


def test_db_add_many(db, sample_action, sample_student_action, sample_employee_action):
    actions = [sample_action, sample_student_action, sample_employee_action]
    db.add_many(actions)
    assert db.count() == 3


def test_db_find_by_plate(db, sample_action, sample_student_action):
    db.add(sample_action)
    db.add(sample_student_action)

    results = db.find_by_plate("а123вс77")
    assert len(results) == 2
    assert results[0]["plate"] == "А123ВС77"

    not_found = db.find_by_plate("О000ОО00")
    assert not_found == []


def test_db_clear(db, sample_action):
    db.add(sample_action)
    assert db.count() == 1
    db.clear()
    assert db.count() == 0
    assert db.get_all() == []


def test_db_print_all(db, sample_action, capsys):
    db.add(sample_action)
    db.print_all()
    captured = capsys.readouterr()
    assert "А123ВС77" in captured.out
