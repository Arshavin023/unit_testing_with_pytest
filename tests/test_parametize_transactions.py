import pytest
import source.shapes as shapes
import source.bank_transactions as bank_transactions
import math

# Parametized test for UserActivity
@pytest.mark.parametrize("customer_id, expected_balance",
                         [("1",2005000),("2",2005000),("3",150000),
                          ("4",85000000),("5",9000000)])
def test_multiple_balance(customer_id, expected_balance):
    assert bank_transactions.Transaction(customer_id).balance() == expected_balance

@pytest.mark.parametrize("customer_id, deposit_amount, expected_balance",
                         [("1",5000, 2010000),("2",1000,2006000),("3",150000,300000),
                          ("4",500000,85500000),("5",10000,9010000)])
def test_multiple_deposit(customer_id, deposit_amount, expected_balance):
    assert bank_transactions.Transaction(customer_id).deposit(deposit_amount) == expected_balance

@pytest.mark.parametrize("customer_id, withdrawal_amount, expected_balance",
                         [("1",5000, 2005000),("2",1000,2005000),("3",50000,250000),
                          ("4",5500000,80000000),("5",10000,9000000)])
def test_multiple_withdrawal(customer_id, withdrawal_amount, expected_balance):
    assert bank_transactions.Transaction(customer_id).withdrawal(withdrawal_amount) == expected_balance

@pytest.mark.parametrize("customer_id, airtime_amount, other_phone_number, expected_balance",
                         [("1",1000,"08143408954", 2004000),("2",5000,"08143508954",2000000),("3",5000,"08143408959",245000),
                          ("4",5000,"08143418954",79995000),("5",10000,"08143428954",8990000)])
def test_multiple_airtime_recharge(customer_id, airtime_amount, other_phone_number, expected_balance):
    assert bank_transactions.Transaction(customer_id).airtime_purchase(airtime_amount, other_phone_number) == expected_balance