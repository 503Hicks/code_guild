#lab 25 ATM

# # 
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:



class ATM:
    def __init__(self, check_balance, deposit, check_withdrawal, calc_interest): #this argument will take on self.
        self.check_balance = check_balance
        self.deposit = deposit

    
    def check_balance(): # returns the account ballance
        pass

    def deposit(amount): # deposits the givin amount in the account
        self.amount = amount
    
    def check_withdrawal(amount): # returns true if the withdraw amount wont put the account in the negative
        self.amount = amount

    def withdraw(amount): # withdraws the amount from the account and returns it
        pass

    def calc_interest(): # returns the amount of interest calculated on the account.
        pass
