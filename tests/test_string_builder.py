from lib.string_builder import *

def test_string_builder_returns_str():
    test_string = StringBuilder()
    test_string.add("Jon")
    result = test_string.output()
    assert result == "Jon"


def test_string_builder_returns_3_for_jon():
    test_string = StringBuilder()
    test_string.add("Jon")
    result = test_string.size()
    assert result == 3
    