from bank import value


def test_value_happy():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("what's up?") == 100


def test_value_panctuations():
    assert value(",") == 100
    assert value("h.,?!;:-'/") == 20
    assert value(".,?!;h:-'/") == 100
    assert value(".,?!;:-'/h") == 100
    assert value("hello.,?!;:-'/") == 0
    assert value(".,?!;hello:-'/") == 100
    assert value(".,?!;:-'/hello") == 100


def test_value_numbers():
    assert value("1636hello") == 100
    assert value("he16ll36o") == 20
    assert value("hello1636") == 0
    assert value("h1636") == 20
    assert value("16h36") == 100
    assert value("1636h") == 100