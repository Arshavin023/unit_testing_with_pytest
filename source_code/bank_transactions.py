class UserActivity:
    def balance(self):
        pass

    def withdrawal(self):
        pass

    def deposit(self):
        pass 

    def update(self):
        pass

class Transaction(UserActivity):
    database = {
        "1": {"first_name": "Uche", "last_name": "Nnodim", "Phone Number": "08167164325", "occupation": "Data Engineer", "balance": 203000},
        "2": {"first_name": "Jerry", "last_name": "Agulehi", "Phone Number": "08036098357", "occupation": "M & E Specialist", "balance": 2005000},
        "3": {"first_name": "Amara", "last_name": "Agulehi", "Phone Number": "08137164325", "occupation": "MakeUp Artist", "balance": 150200}
    }

    def __init__(self, customer_id: str):
        self.customer_id = customer_id

    def balance(self):
        return self.database[self.customer_id]["balance"]

    def deposit(self, deposit_amount: float):
        print(f"Account balance before deposit: {self.balance()}")
        self.database[self.customer_id]["balance"] += deposit_amount
        print(f"Account balance after deposit: {self.balance()}")
        return self.balance()

    def withdrawal(self, withdrawal_amount: float):
        print(f"Account balance before withdrawal: {self.balance()}")
        if self.balance() - withdrawal_amount >= 100:
            print("Sufficient balance available, withdrawal ongoing")
            self.database[self.customer_id]["balance"] -= withdrawal_amount
            print(f"Account balance after withdrawal: {self.balance()}")
            return self.balance()
        else:
            print(f"Withdrawal impossible due to insufficient balance or withdrawal amount too high")
    
    def airtime_purchase(self, airtime_amount: float, other_phone_number: str):
        print(f"Account balance before airtime purchase: {self.balance()}")
        if self.balance() - airtime_amount >= 100:
            print("Sufficient balance available, airtime recharge possible")
            if other_phone_number != self.database[self.customer_id]['Phone Number']:
                print(f"{airtime_amount} airtime will be recharged on {other_phone_number}")
            else:
                print(f"{airtime_amount} will be recharged for self: {self.database[self.customer_id]['Phone Number']}")
            self.database[self.customer_id]["balance"] -= airtime_amount
            print(f"Account balance after airtime purchase: {self.balance()}")
            return self.balance()
        else:
            print(f"Airtime recharge impossible due to insufficient balance or recharge amount too high")
