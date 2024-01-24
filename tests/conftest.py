import pytest
import source.bank_transactions as bank_transactions

@pytest.fixture
def first_customer():
    return bank_transactions.Transaction(1)

@pytest.fixture
def second_customer():
    return bank_transactions.Transaction(2)

@pytest.fixture
def third_customer():
    return bank_transactions.Transaction(3)