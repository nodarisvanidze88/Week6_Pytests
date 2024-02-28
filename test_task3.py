from task3 import calculate_interest
import pytest

def test_calculate_interest():
    assert calculate_interest(1000, 5, 10) == 500
    assert calculate_interest(1000, 0, 10) == 0

def test_valueError():
    with pytest.raises(ValueError) as errorMessage:
        calculate_interest(1000, 0, 150)
        calculate_interest(1000, 0, 200)
    assert str(errorMessage.value) == "Percent should be less than or equal to 100"

