class UserActivity:
    def balance(self):
        pass
    def withdrawal(self):
        pass
    def deposit(self):
        pass 
class Transaction(UserActivity):
    database = {
        1 : {"first_name": "Uche", "last_name": "Nnodim","full_name":"Uche Nnodim", "Phone Number": "08104164129",
               "occupation": "Data Engineer", "balance": 2005000},
        2 : {"first_name": "Jerry", "last_name": "Agulehi","full_name":"Jerry Agulehi", "Phone Number": "08036098357", 
              "occupation": "M & E Specialist", "balance": 2005000},
        3 : {"first_name": "Amara", "last_name": "Agulehi","full_name":"Amara Agulehi", "Phone Number": "08137164325", 
              "occupation": "MakeUp Artist", "balance": 150000},
        4 : {"first_name": "Alex", "last_name": "Adogwa","full_name":"Alex Adogwa", "Phone Number": "08139164325", 
              "occupation": "Doctorate Student", "balance": 85000000},
        5 : {"first_name": "Michael", "last_name": "Asuquo","full_name":"Michael Asuquo", "Phone Number": "08137164328", 
              "occupation": "Engineering Manager", "balance": 9000000}
    }

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        
    def get_user_information(self):
        return self.database.get(self.customer_id)
    
    def balance(self):
        return self.get_user_information()['balance']
        # return self.database[self.customer_id]["balance"]

    def deposit(self, deposit_amount: float):
        print(f"Account balance for {self.get_user_information()['full_name']} before deposit: {self.balance()}")
        self.database[self.customer_id]["balance"] = self.balance() + deposit_amount
        print(f"Account balance for {self.get_user_information()['full_name']} after {deposit_amount} deposit: {self.balance()}")
        return self.balance()

    def withdrawal(self, withdrawal_amount: float):
        print(f"Account balance for {self.get_user_information()['full_name']} before withdrawal: {self.balance()}")
        if self.balance() - withdrawal_amount >= 100:
            print("Sufficient balance available, withdrawal ongoing")
            self.database[self.customer_id]["balance"] = self.balance() - withdrawal_amount
            print(f"Account balance for {self.get_user_information()['full_name']} after {withdrawal_amount} withdrawal: {self.balance()}")
            return self.balance()
        else:
            print(f"Withdrawal impossible due to insufficient balance or withdrawal amount too high")
    
    def airtime_purchase(self, airtime_amount: float, other_phone_number: str):
        print(f"Account balance for {self.get_user_information()['full_name']} before airtime purchase: {self.balance()}")
        if self.balance() - airtime_amount >= 100:
            print("Sufficient balance available, airtime recharge possible")
            if other_phone_number != self.database.get(self.customer_id)['Phone Number']:
                print(f"{airtime_amount} airtime will be recharged on {other_phone_number}")
            else:
                print(f"{airtime_amount} will be recharged for self: {self.database.get(self.customer_id)['Phone Number']}")
            self.database[self.customer_id]["balance"] = self.balance() - airtime_amount
            print(f"Account balance for {self.get_user_information()['full_name']} after airtime purchase: {self.balance()}")
            return self.balance()
        else:
            print(f"Airtime recharge impossible due to insufficient balance or recharge amount too high")

# test = Transaction(1)
# print(test.get_user_information())
# print(test.balance())
# print(test.deposit(1000))
# print(test.withdrawal(1000000))
# print(test.airtime_purchase(6000,"08030000000"))