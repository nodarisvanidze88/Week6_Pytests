from task2 import choise, numChecker, get_distance, get_speed, get_time
from unittest.mock import patch
import pytest


def test_get_distance():
    assert get_distance(100, 5) == 500
    assert get_distance(20, 10) == 200

def test_get_speed():
    assert get_speed(100, 5) == 20
    assert get_speed(20, 10) == 2

def test_get_time():
    assert get_time(100, 5) == 20
    assert get_time(20, 10) == 2

@patch("builtins.input", side_effect = ["1","2","3","cat"])
def test_choise(mock_input):
    assert choise() == "1"
    assert choise() == "2"
    assert choise() == "3"
    with pytest.raises(StopIteration):
        assert choise() == None


@patch("builtins.input", side_effect = ["100","200","sdfjsadfj"])
def test_numChecker(mock_input):
    assert numChecker("Give us the speed") == 100
    assert numChecker("Give us the speed") == 200
    with pytest.raises(StopIteration):
        assert numChecker("Give us the speed") == None

