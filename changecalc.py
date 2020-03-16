# Lab 8: Make Change

# Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Concepts Covered

# conditionals, comparisons
# arithmetic
# Version 1

# Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

# Version 2

# Have the user enter a dollar amount (1.36), convert this to the total in pennies.


print("Change calculator")

#USER INPUT OF CHANGE
change = float(input("Please enter an amount of change: "))

#CHANGE VALUES
quarters = .25
dimes = .10
nickles = .05
pennies = .01
#AMOUNT OF CHANGE RETURNED
numberQ = change//quarters 
change2 = (change%quarters)
numberD = change2//dimes 
change3 = (change2%dimes)
numberN = change3//nickles
change4 = (change3%nickles)
numberP = change4//pennies
#AMOUNT OF CHANGE IN PENNIES
penny_change = change*100 

print(f'\nyour change in pennies is {penny_change}')

print(f' \nOrrrrrr: \n{numberQ} quarters, \n{numberD} dimes, \n{numberN} nickles, \naaaaaand.... \n{numberP} pennies.')
# print(numberQ)
# print(numberD)
# print(numberN)
# print(numberP)
