from lib.gratitudes import *

def test_gratitudes_returns_formatted_string():
    str1 = Gratitudes()
    result = str1.format()
    assert result == "Be grateful for: "

def test_gratitudes_joins_formatted_string_with_item_from_list():
    str1 = Gratitudes()
    str1.add("music")
    result = str1.format()
    assert result == "Be grateful for: music"

def test_gratitudes_joins_formatted_string_with_multiple_from_list():
    str1 = Gratitudes()
    str1.add("music")
    str1.add("love")
    str1.add("romance")
    result = str1.format()
    assert result == "Be grateful for: music, love, romance"