from lib.report_length import *

def test_report_length_has_accurate_length_for_3_letter_word():
    result = report_length("Jon")
    assert result == "This string was 3 characters long."

def test_report_length_has_accurate_length_for_4_letter_word():
    result = report_length("shop")
    assert result == "This string was 4 characters long."

def test_report_length_has_accurate_length_for_5_letter_word():
    result = report_length("funny")
    assert result == "This string was 5 characters long."

def test_report_length_has_accurate_length_for_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."