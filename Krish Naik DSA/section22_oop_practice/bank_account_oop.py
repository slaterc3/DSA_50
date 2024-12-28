class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        self.balance += amount 
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal")
        else:
            self.balance -= amount 
    
    def transfer(self, other, amount):
        if amount < self.balance:
            self.withdraw(amount)
            other.deposit(amount)
        else:
            print("Insufficient funds for transfer")
            
            
acc1, acc2 = BankAccount("John Doe", 1000), BankAccount("Jane Smith", 2000)

assert acc1.balance == 1000 
assert acc2.balance == 2000 
acc1.deposit(500) 
acc2.withdraw(100) 
acc1.transfer(acc2, 200) 
print(acc1.balance, acc2.balance)
assert acc1.balance == 1300 
assert acc2.balance == 2100 
# # Test Case 2: 
acc3, acc4 = BankAccount("Alice Johnson", 500),BankAccount("Bob Brown", 1500) 
assert acc3.balance == 500 
assert acc4.balance == 1500 
acc3.deposit(100) 
acc4.withdraw(200) 
acc3.transfer(acc4, 300) 
assert acc3.balance == 300 
assert acc4.balance == 1600


