
class BankAccount:
    def __init__ (self, bal=0):
        self.account_balance = bal

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            return self.account_balance
        else:
           return False
     
    def display_balance(self):
        return print(f"Current Balance: {self.account_balance}")