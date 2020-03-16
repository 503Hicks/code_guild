# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

# Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

# Version 2

# Allow the user to enter the value of n, remember to convert its type, as input returns a string.

# Version 3 (optional)

# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. Generate a password accordingly.



import random
import string


# length = int(input("\nHow long would you many characters would you like your password:"))
uppercase = int(input('How many uppercase letters would you like in your password? '))
lowercase = int(input('how many lowercase letters would you like in your password? '))
numbers = int(input('How many numbers would you like in your password? '))
special_char = int(input('How many special characters would you like in your password? '))


# letters = string.ascii_letters
uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
digits = string.digits
punctation = string.punctuation
password = [""]

# for i in range(length):
#     password = password + random.choice(letters)

for u in range(uppercase):
    password.append(random.choice(uppers))

for l in range(lowercase):
    password.append(random.choice(lowers))

for d in range(numbers):
    password.append(random.choice(digits))

for p in range(special_char):
    password.append(random.choice(punctation))

random.shuffle(password)

print(''.join(password))








# letters = string.ascii_letters
# digits = random.choice(digits)
# punctuation = ra
# # digits = string.ascii_digits
# # punctuation = string.ascii_punctuation
# password = ""

# for i in range(10):
#     password = password + random.choice(letters)
# print(password)