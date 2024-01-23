import pytest


def test_balance(first_customer):
    assert first_customer.balance() == 2005000

def test_deposit(second_customer):
    assert second_customer.deposit(150000) == 2155000
    
def test_withdrawal(third_customer):
    assert third_customer.withdrawal(50000) == 100000

def test_airtime_purchase(first_customer):
    assert first_customer.airtime_purchase(1000,'08030000000') == 2004000
    