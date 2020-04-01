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
        self.balance = self.balance + amount
        return f'You deposited {amount} dollars. your new amount is {self.balance}'

    def check_withdrawal(self, amount): # check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the
        if amount < self.balance:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        return f'You withdrew {amount} dollars. your new amount is {self.balance}'
   
   
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account



my_atm1 = ATM(3000,[])

print(my_atm1.check_balance())
print(my_atm1.deposit(4582))
print(my_atm1.check_balance())
print(my_atm1.check_withdrawal(20))
print(my_atm1.withdraw(100))
print(my_atm1.withdraw(100))
print(my_atm1.withdraw(100))
