# Practice: Strings

# For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

# def add(a, b):
#     return a + b
# #print(add(5, 2))
# #print(add(8, 1))

import string
import ascii 


# Problem 1

# Get a string from the user, print out another string, doubling every letter.


def double_letter():
    user_input = 'enter string to be doubled: '
    double_input = ''

    for i in user_input:
        double_input = i + i
    return double_in


# I would probably do it this way:

# >>> dup = "abc"
# >>> dup1 = str()  # a new, empty string.
# >>> for char in dup:
# ...    dup1 += char + char  # strings concatenate using + and +=


# def double_letter():
#     user_string = input('Enter string to be doubled: ')
#     for i in user_string:
#       print(i*2, end='')
# double_letter()
    

# Problem 2

# Write a function that takes a string, and returns a list of strings, each missing a different character.

def missing_char():
    user_string = 'kitten'

    for i in len(user_string):
        user_string.append(user_string)

        print(user_string)

# Problem 3

# Return the letter that appears the latest in the english alphabet.

# >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
# the latest letter is v.

def get_latest_letter():
    letters = letters.ascii.
    latest_letter = 'pneumonoultramicroscopicsilicovolcanoconiosis'
    checks = 




