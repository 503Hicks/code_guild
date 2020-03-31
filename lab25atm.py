#lab 25 ATM

# # 
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:



class ATM():
    def __init__(self, balance=0, print_transactions=[]):
        self.balance = balance
        self.print_transactions = print_transactions

        
    def check_balance(self): # returns the account ballance
        return f' your balance is {self.balance}'

    def deposit(self, amount):
        return self.balance + amount
   
    # deposit(amount) deposits the given amount in the accoun

my_atm = ATM()

print(my_atm.check_balance())
print(my_atm.deposit(4582))
print(my_atm.check_balance())
