import string


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
        self.balance = self.balance - amount
        self.print_transcations = self.print_transactions.append(f'You withdrew {amount}')
        return f'You withdrew {amount} dollars. your new amount is {self.balance}'
    def get_trasactions(self):
        return self.print_transactions

def main():
    my_atm1 = ATM(3000,[])
# while loop

    while True:
        
        user_selection = input('what would you like to do (deposit, withdraw, balance, history, or Cancel)? ')
        
        if user_selection == 'deposit':
            user_amount = float(input('how much? ' ))
            print(my_atm1.deposit(user_amount))
        if user_selection == 'withdraw':
            user_amount = float(input('how much? ' ))
            print(my_atm1.withdraw(user_amount))
        if user_selection == 'balance':
            print(my_atm1.balance)
        if user_selection == 'history':
            print(my_atm1.print_transactions)
        if user_selection == 'cancel':
            print('Thank you for using. Goodbye! ')
            break
            

main()



    # print(my_atm1.check_balance())
    # print(my_atm1.deposit(500))
    # print(my_atm1.deposit(1000))
    # print(my_atm1.deposit(25))
    # print(my_atm1.withdraw(2000))
    # print(my_atm1.withdraw(2000))
    # print(my_atm1.get_trasactions())
    # print(my_atm1.check_balance())
    

