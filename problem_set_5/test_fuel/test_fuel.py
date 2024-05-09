from fuel import main, convert, gauge
import pytest


def test_convert_to_percentage():
    assert convert("2/100") == 2
    assert convert("1/10") == 10
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("9/10") == 90
    assert convert("98/100") == 98


def test_convert_empty_full():
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("199/200") == 100


def test_convert_round():
    assert convert("7/8") == 88
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"


def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error_exception():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_type_error_exception():
    with pytest.raises(ValueError):
        convert("1.5/8.3")