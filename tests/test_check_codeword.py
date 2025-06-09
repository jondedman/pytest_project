from lib.check_codeword import *

def test_check_codeword_returns_comein_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_returns_close_for_hope():
    result = check_codeword("hope")
    assert result == "Close, but nope."

def test_check_codeword_returns_wrong_for_makers():
    result = check_codeword("makers")
    assert result == "WRONG!"