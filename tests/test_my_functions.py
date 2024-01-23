import pytest 
import source_code.my_functions as my_functions

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


