class ATM():
    def __init__(self, balance=0, print_transactions=[]):
        self.balance = balance
        self.print_transactions = print_transactions
    
    def check_balance(self): # returns the account ballance
        return f'****Your balance is {self.balance}****'

    def deposit(self, amount): 
        self.balance = self.balance + amount
        self.print_transcations = self.print_transactions.append(f'You deposited {amount}')
        return f'You deposited {amount} dollars. your new amount is {self.balance}'
    

    def check_withdrawal(self, amount):#returns true if the withdrawn amount won't put the account in the neg.
        if amount < self.balance:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return f'You withdrew {amount} dollars. your new amount is {self.balance}'
    
    def get_trasactions(self):
        return self.print_transactions

my_atm1 = ATM(3000,[])

print(my_atm1.check_balance())
print(my_atm1.deposit(500))
print(my_atm1.deposit(1000))
print(my_atm1.deposit(25))
# print(my_atm1.print_transactions)

print(my_atm1.get_trasactions())
