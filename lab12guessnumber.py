# Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

# Concepts Covered

# random.randint
# REPL: read-evaluate-print loop
# input, print
# Version 1

# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

# import random
# x = random.randint(1,10)
# print(x)
# Below is an example run of the game:

# guess the number: 5
# try again!
# guess the number: 2
# try again!
# guess the number: 3
# correct! you guessed 3 times
# Version 2

# Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.

# Version 3

# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

# Version 4 (optional)

# Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

# Version 5 (optional)

# Swap the user with the computer: the user will pick a number, and the computer will make random guesses until they get it right.

# import random
# #COMPUTERS RANDOM NUMBER BETWEEN 1-10
# number = random.randint(1, 10)
# attempts=0

# #MAX ATTEMPTS OF 10
# while (attempts < 10):
#     #USERS # OF ATTEMPTS 
#     attempts = attempts+1
#     #USERS GUESS
#     current_guess = int(input('Guess a number: '))

#     #RESPONSE TO USERS GUESS
#     if current_guess == number:
#         print(f'You guessed correct in {attempts} tries!')
#         break
#     elif current_guess < number:
#         print('You guessed to low... try again.')
#     else:
#         print('you guessed too high... try again.')
       




import random
#Computers random number 1-10
number = random.randint(1, 10)

attempts=0
last_guess = 0

while (attempts < 10):
    attempts = attempts+1

    current_guess = int(input('Guess a number: '))
    

    if current_guess == number:
        print(f'You guessed correct in {attempts} tries!')
        break
    elif current_guess != number:
        print('Try again.')
        if abs(number - current_guess) < abs(number - last_guess):
            print("You're getting warmer")
        else:
            print("You're getting colder.")
    last_guess = current_guess
