import pytest
from lib.password_checker import *

def test_password_checker_validates_length():
    checker = PasswordChecker()
    result = checker.check("12345678")
    assert result == True

def test_password_checker_returns_exception_error_for_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        checker.check("123456")
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."


