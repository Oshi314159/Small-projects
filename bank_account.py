class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def display_balance(self):
        print(f"Your balance: ${self.balance}")
        
James = BankAccount("James", "Crack", 20090325, "Checking", 5959372, 300)
print(f"James deposited $96 and his current balance is {James.deposit(96)}")
print(f"James withdrew $25 and his current balance is {James.withdraw(25)}")
James.display_balance()
