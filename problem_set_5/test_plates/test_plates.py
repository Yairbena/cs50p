from plates import is_valid


def test_is_valid_lengh():
    assert is_valid("") == False
    assert is_valid("a") == False
    assert is_valid("ab") == True
    assert is_valid("abc") == True
    assert is_valid("abcd") == True
    assert is_valid("abcde") == True
    assert is_valid("abcdef") == True
    assert is_valid("abcdefg") == False
    assert is_valid("abcdefghijklmnopqrstuvwxyz") == False


def test_is_valid_starts_with_alpha():
    assert is_valid("ab") == True
    assert is_valid("a-") == False
    assert is_valid("-a") == False
    assert is_valid("a,") == False
    assert is_valid(",a") == False
    assert is_valid(".|") == False
    assert is_valid("a1") == False
    assert is_valid("1a") == False
    assert is_valid("12") == False


def test_is_valid_panctuation_and_space():
    assert is_valid(",-!|':") == False
    assert is_valid("ab,123") == False
    assert is_valid("ab 123") == False
    assert is_valid("ab123 ") == False
    assert is_valid(" ab123") == False
    assert is_valid("ab12,") == False
    assert is_valid("ab1.") == False
    assert is_valid("ab}") == False


def test_is_valid_end_with_number():
    assert is_valid("ABCDE1") == True
    assert is_valid("ABCD10") == True
    assert is_valid("ABC102") == True
    assert is_valid("AB1002") == True
    assert is_valid("AB120") == True
    assert is_valid("AB10") == True
    assert is_valid("AB1") == True


def test_is_valid_sequential_numbering():
    assert is_valid("AB1234") == True
    assert is_valid("AB12") == True
    assert is_valid("AB1C23") == False
    assert is_valid("ABC12") == True
    assert is_valid("AB100i") == False


def test_is_valid_numbers_starts_with_zero():
    assert is_valid("AB0") == False
    assert is_valid("AB01") == False
    assert is_valid("AB001") == False
    assert is_valid("AB0001") == False
    assert is_valid("AB0012") == False
    assert is_valid("AB0123") == False