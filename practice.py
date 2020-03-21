# nouns = input("give three nounds seperated by a space")
# nounds_list = nouns.split(', ')

# adj1 = input("Enter an adjective: ")
# adj2 = input("Enter another adjective: ")
# bird = input("Enter a type of bird: ")
# room = input("Enter a room in a house: ")
# verb1 = input("Enter a past tense verb: ")
# verb2 = input("Enter a verb: ")
# verb3 = input("Enter a verb inding in -ing: ")
# verb4 = input("Enter a verb ending in -ing: ")
# name = input("enter a relative's name: ")
# liquid = input("Enter a liquid: ")
# bodypart = input("Enter a part of the body; plural: ")
# noun1 = input("Enter a noun: ")
# noun2 = input("Enter a plural noun: ")
# noun3 = input("Enter a noun: ")


# nounlist = []
# nounlist.append(nouns)


# for i in range(3):
#     nouns = input('enter three nouns')




# print(f'It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs. I {verb1} down the stairs to see if I could help {verb2} the dinner. My mom said, "See if {name} needs a fresh {nouns[0]}." So I carried a tray of glasses full of {liquid} into the {verb3} room. When I got there, I couldn\'t believe my {bodypart}! There were {nouns[1]} {verb4} on the {nouns[2]}')




# user_input = input('do you want to continue?: ')

# while (user_input == 'yes'):
#     print('continuing...')
#     user_input = input('do you want to contiue: ')


# x > 5 and x < 10
# 5 < x < 10

# number = 9876543210
# i = 4
# number[i] # should return 6



    
# print("Welcome to class! ")

# while True:
#     grade = int(input("Please enter your Grade: "))

#     def qualifier():

#         if grade % 10 >= 7:
#             qualifier = "+"
#         elif grade % 10 >= 4:
#             qualifier = " "
#         else:
#             qualifier = "-"
#         return qualifier
    
# # while True:

# # grade = input("please enter student's  score: ")
# # grade = int(grade)

#     if grade >= 90 and grade <=100: 
#         print("A"+ qualifier())

#     elif grade >= 80 and grade <=89: 
#         print("B"+ qualifier())
#     elif grade >= 70 and grade <=79:
#         print("C"+ qualifier())
#     elif grade >= 60 and grade <= 69:
#         print("D"+ qualifier)
#     elif grade >= 0 and grade <= 59:
#         print("You got an F!")
#     else:
#         print("you cheater!")

#     if(input('\nWould you like to make another (y/n): ').lower() != 'y'):
        
#         print('I don\'t blame you. Fuck them kids')
#         break


# from random import choice


# while True:

    # welcome = "welcome to the 8 Ball"
    # print(welcome)

#enter "done" to exit program
    # if(input("\nAsk me a qustion! ").lower() == "done"):
        
    #     print('\nokay, have a good one!')
    #     break

    # input("ASK A QUESTION! ")


    # response= ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "Most likely", "Yes", "Signs point to yes", "Reply hazy try again", "Better not tell you now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My source says no", "Outlook not so good", "Very doubtful"]


    # print(choice(response))

    # if(input('\nEnter "Done" to exit: ').lower() == 'done'):
        
    #     print('Cool... Later brah')
    #     break




import random
import string


# length = int(input("\nHow long would you many characters would you like your password:"))
# uppercase = int(input('How many uppercase letters would you like in your password? '))
# lowercase = int(input('how many lowercase letters would you like in your password? '))
# numbers = int(input('How many numbers would you like in your password? '))
# special_char = int(input('How many special characters would you like in your password? '))

# length = ''.join()

# random.shuffle()

# letters = string.ascii_letters
# upper = ''.join(random.choice(string.ascii_uppercase)
# lower = ''.join(random.choice(string.ascii_lowercase))
# digits = ''.join(random.choice(string.digits))
# punctation = ''.join(random.choice(string.punctuation))
# password = ""



# lower = ''.join(random.choice(string.ascii_lowercase) * lowercase)
# upper = ''.join(random.choice(string.ascii_uppercase) * uppercase)
# number = ''.join(random.choice(string.digits) * numbers)
# punct = ''.join(random.choice(string.punctuation) * special_char)
# p = lower + upper + number + punct
# print(''.join(random.shuffle(p)))



# for i in range(length):
#     password = password + random.choice(letters)





# print('\n' + password)


# def trivial():
#     print('something')

# x = trivial()
# print(dir(trivial))

# make sure to () around function to call it




# import random
# import string


# length = int(input("\nHow long would you many characters would you like your password:"))
# uppercase = int(input('How many uppercase letters would you like in your password? '))
# lowercase = int(input('how many lowercase letters would you like in your password? '))
# numbers = int(input('How many numbers would you like in your password? '))
# special_char = int(input('How many special characters would you like in your password? '))



# letters = string.ascii_letters
# uppers = string.ascii_uppercase
# lowers = string.ascii_lowercase
# digits = string.digits
# punctation = string.punctuation
# password = ""

# new_pass = uppercase + lowercase + numbers + special_char


# for i in range(new_pass):
#     password = password + random.shuffle(new_pass)

# print(password)


# import random
# import string


# choices = ['rock', 'paper', 'scissors']
# play_again = 'yes'


# while play_again == 'yes':


#     user_choice = input("Rock, paper, scissors?").lower()
#     comp_choice = random.choice(choices)


#     print(f"{user_choice} vs {comp_choice}")


#     if user_choice == comp_choice:
#         print('Its a tie!')
#     elif user_choice == 'rock' and comp_choice == 'paper':
#         print('Paper covers rock... YOU LOSE!!')
#     elif user_choice == 'rock' and comp_choice == 'scissors':
#         print('Rock smashes scissors... YOU WIN!!!')
#     elif user_choice == 'paper' and comp_choice == 'rock':
#         print('Paper covers rock... YOU WIN!!!')
#     elif user_choice == 'paper' and comp_choice == 'scissors':
#         print('Scissors cuts paper... YOU LOSE!!!')
#     elif user_choice == 'scissors' and comp_choice == 'rock':
#         print('Rock smashes scissors... YOU LOSE!!!')
#     elif user_choice == 'scissors' and comp_choice == 'paper':
#         print('Scissors cuts paper... YOU WIN!!!')

#     play_again = input('Would you like to play again?').lower()
# else:
#     print("thanks for playing!")



# a = 168%25
# b = 168//25
# print(a)
# print(b)


# v1 = 'I told my friend, "python is my favorite language!" '


# print(v1)
# print(v1.title())
# print(v1.lower())


# The .lower() medthod is particularly useful for storing data. Many times you wont want to trust the capitalization that your users provide, so youll convert strings to lowercase before storing them.

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = f'Hello, {first_name.title()} {last_name.title()}!'

# print(f'Oh {full_name}')

# print('Languages:\nC\npython\nJavaScript')


# favoreite_language = '     python     3'

# print(favoreite_language.rstrip())
# print(favoreite_language.lstrip())
# print(favoreite_language.strip())



# import random

# created my main function

# created a list of valid moves

# reate a list of tuples that represent valid winning cases 

# while the user wants to keep playing

#     ask the user for a move 
#     if the user chooses 'q' i quit

# chose a move for the computer by pickeing an element oyt of the valid moves
#     list

# create a tuple out of the users move and the computers move, (users move, computers move)

# used conditionals to check 
#     if the user move is not in valid moves, tell them to try again or quit
#     if the users move is the same as the computers move, tell them they tied
#     if the typle (users move, computers move) is in the list of tuples that contain the possible combinations of winning moves, tell  the user they won.
#     else, tell the user theyre a loser and they got beat by a bunch of melted sand with fancy patters on imported.

# product_to_price = {'apple': 1.0, 'pear': 1.5, 'grapes':0.75}

# print(product_to_price['apple'])

# product_to_price['apple']= 300
# print(product_to_price['apple'])
# print(product_to_price['grapes'])

# product_to_price['avacado'] = 50000000000


# if 'apple' in product_to_price:
#     print('apple ' + str(product_to_price['apple']))


# product_to_price.update({'banana': 0.25})
# print(product_to_price)


# print(list(product_to_price.keys()))
# print(list(product_to_price.values()))
# print(list(product_to_price.items()))



# names_and_colors = [('alice', 'red'),('david', 'green')]
# new_dict = dict(names_and_colors)
# print(new_dict)

# from_units = meters.get(input('Enter your unit'))





# meters = {
# 'in': 0.0254,
# 'ft': 0.348,
# 'yd': 0.9144,
# 'm': 1,
# 'mi': 1609.34,
# 'km': 1000,
# }

# distance = int(input('Enter a distance: '))
# start_units = input('Enter type of units: ')
# end_units = meters.get(input('Enter the unit you would like to convert to: '))


# m = 1
# ft = (m * distance) * 0.3048
# mi = (m * distance) * 1609.34
# km = (m * distance) * 1000
# yd = (m * distance) * 0.9144
# inch = (m * distance) * 0.0254


# if start_units == 'ft':
#     print(f'{distance}{start_units} is {ft}m')
#     foot_dist = ft/ft
#     print(end_units)
# elif start_units == 'mi':
#     print(f'{distance}{start_units} is {mi}m')
#     mi_dist = mi/end_units
#     print(mi_dist)
# elif start_units == 'km':
#     print(f'{distance}{start_units} is {km}m')
#     km_dist = km/end_units
#     print(km_dist)
# elif start_units == 'yd':
#     print(f'{distance}{start_units} is {yd}m')
#     yd_dist = yd/end_units
#     print(yd_dist)
# elif start_units == 'in':
#     print(f'{distance}{start_units} is {inch}m')
#     inch_dist = inch/end_units
#     print(inch_dist)


# define up_top
#     define a function that takes in a distance, amd a unit and returns the distacne converted into the specified unit

#     func(dist, unit):
#         if unit == m
#             func(dist, unit) distance * conversion_factot
#         elif unit == ft
#             distance * conversion factor for ft



#             define a functin that convers the given distance (specified in meteres) into the target units.


#             define another funtion that standardizes the units


#             define main(

#                 ask for the distance
#                 convert the distance to a float


#                 loop, while true is one way to do into
#                     ask the user for the units to convert from 
#                     ask the user for the units to convert to

#                     convert the distance to meters 
#                     use the distance converted to m, to then convert into the target unit.
#                     assk if the user wants to go again
#                     if y, go again
#                     in no, break
#             )



# def a_function():
#     x = 5
#     y = 3
#     def another_function():
#         x = 5
#         z = 2
#         print(y)

# import random
# #Computers random number 1-10
# number = random.randint(1, 10)

# attempts=0
# last_guess = 0

# while (attempts < 10):
#     attempts = attempts+1

#     current_guess = int(input('Guess a number: '))
    

#     if current_guess == number:
#         print(f'You guessed correct in {attempts} tries!')
#         break
#     elif current_guess != number:
#         print('Try again.')
#         if abs(number - current_guess) < abs(number - last_guess):
#             print("You're getting warmer")
#         else:
#             print("You're getting colder.")
#     last_guess = current_guess




# abc = " abcdefghijklmnopqrstuvwxyz"   

# user_input = input('enter text: ')
# input_len = input('input the amount of rotation')
# rot_output = "".join([abc[(abc.find(i)+len(input_len))%26] for i in user_input])
# print(rot_output)

# rot_output = ''.join([abc])

# for i in user_input:
#     ''.join([abc[abc.find(i) + len(input_len)]])


# print(user_input)
# my version
# y = ''
# user_input = input('enter text: ')
# input_len = input('input the amount of rotation')



# for i in user_input:
#     x = (abc.find(i) + input_len) % 26
#     y += abc[x]

#     print(''.join(y))



nums = [ 4, 56, 73, 12, 17, 99, 42, 87]

# some_list[::]

print(nums[::])
print(nums[3::])
print(nums[2:6:2])
print(nums[::2])
print(nums[::-1])


[(alphabet.index(i) + rotation) % len(alphabet)]


rot = []
for i in alphabet:
    if i in alphabet:
        encrypted = (alphabet.index(i) + rotation) % len(alphabet)
        rot.append(encrypted)

    else: 
        rot.append(i)



random_list = [1,3,4,5, "test", 6, 7, 199]

for random_item in random_list:
         print(random_item)



        rot = []
for i in alphabet:
    if i.lower() in alphabet:
        encrypted = (alphabet.index(i) + rotation) % len(alphabet)
        rot.append(encrypted)

    else: 
        rot.append(i)