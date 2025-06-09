import pytest
from lib.present import *

def test_present_raises_exception_when_present_has_already_been_wrapped():
    present = Present()
    present.wrap("Book")
    with pytest.raises(Exception) as err:
        present.wrap("Toy")
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."

def test_present_raises_exception_when_nothing_to_unwrap():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."
    