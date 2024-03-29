import pytest 
import source.my_functions as my_functions
import time

def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_add_strings():
    result = my_functions.add("I like", " Burgers")
    assert result == "I like Burgers"

def test_divide():
    result = my_functions.divide(10,2)
    assert result == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10,0)

def test_bank_trans(first_customer):
    assert first_customer.balance() == 2005000

@pytest.mark.slow #This notifies that the test will be a slow one
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(10,2)
    assert result == 5

@pytest.mark.skip(reason="This feature is currently broken") #This helps to skip a test
def test_add():
    assert my_functions.add(1, 3) == 3

@pytest.mark.xfail(reason="Division by Zero is impossible")  # This shows that test will definitely fail
def test_divide_zero_broken():
    my_functions.divide(10,0)