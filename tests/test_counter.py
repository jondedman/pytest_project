from lib.counter import *

def test_the_counter_returns_5():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_the_counter_returns_10():
    counter = Counter()
    counter.add(10)
    result = counter.report()
    assert result == "Counted to 10 so far."

def test_the_counter_returns_100():
    counter = Counter()
    counter.add(100)
    result = counter.report()
    assert result == "Counted to 100 so far."