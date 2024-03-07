from twttr import shorten

def test_shorten():
    assert shorten("AEIOUaeiou") == ""
    assert shorten("Once a WhilE thEre is AN Issue") == "nc  Whl thr s N ss"
    assert shorten("4ddu(jJJ) HHy& JKl") == "4dd(jJJ) HHy& JKl"
    assert shorten("Be thE ONE") == "B th N"
    assert shorten("73hN 33th ERrroR") == "73hN 33th RrrR"


