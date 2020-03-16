
# Print a welcome screen to the user.
# Use the random module's random.choice() to choose a prediction.
# Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
# Display the result of the 8-ball.
# Below are some example 'predictions':

# It is certain
# It is decidedly so
# Without a doubt
# Yes definitely
# You may rely on it
# As I see it, yes
# Most likely
# Outlook good
# Yes
# Signs point to yes
# Reply hazy try again
# Ask again later
# Better not tell you now
# Cannot predict now
# Concentrate and ask again
# Don't count on it
# My reply is no
# My sources say no
# Outlook not so good
# Very doubtful
# Version 2

# Using a while loop, keep asking the user for a question, if they enter 'done', exit



import random


while True:

    welcome = "\nwelcome to the 8 Ball"
    print(welcome)

    # USER QUESTION
    input("\nAsk me a qustion! ")

    # RESPONSE OUTPUT
    response= ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "Most likely", "Yes", "Signs point to yes", "Reply hazy try again", "Better not tell you now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My source says no", "Outlook not so good", "Very doubtful"]

    # PRINT OUTPUT
    print('\n' + random.choice(response))

    if(input('\nEnter "Done" to exit: ').lower() == 'done'):
        
        print('Cool... Later brah')
        break

