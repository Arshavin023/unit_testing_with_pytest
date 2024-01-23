import pytest
import source_code.bank_transactions as bank_transactions
import math

class TestDeposit:
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.transaction = bank_transactions.Transaction("2")
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
    
    def test_balance(self):
        assert self.transaction.balance() == 2005000

    def test_deposit(self):
        assert self.transaction.deposit(150000) == 2155000
        
    def test_withdrawal(self):
        assert self.transaction.withdrawal(150000) == 2005000
    
    def test_airtime_purchase(self):
        assert self.transaction.airtime_purchase(1000,'08030000000') == 2004000
    