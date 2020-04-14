# Lab 3: Grading

# Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

# Instructions

# Have the user enter a number representing the grade (0-100)
# Convert the number grade to a letter grade
# Numeric Ranges

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F


# Version 2

# Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.

# Version 3

# Extract the logic used to determine the grade and its qualifier ('+', '-', or ' ') into functions. Additionally, use a while loop to repeatedly ask the user if they'd like to compute another grade after each computation.


print("Welcome to class! ")

while True:
    #TO GET USERS GRADE NUMBER
    grade = int(input("Please enter your Grade: "))
    
    #TO GET USERS QUALIFIER
    def qualifier():

        if grade % 10 >= 7:
            qualifier = "+"
        elif grade % 10 >= 4:
            qualifier = " "
        else:
            qualifier = "-"
        return qualifier
    #TO GET USERS LETTER GRADE
    if grade >= 90 and grade <=100: 
        print("A"+ qualifier())
    elif grade >= 80 and grade <=89: 
        print("B"+ qualifier())
    elif grade >= 70 and grade <=79:
        print("C"+ qualifier())
    elif grade >= 60 and grade <= 69:
        print("D"+ qualifier())
    elif grade >= 0 and grade <= 59:
        print("You got an F!")
    else:
        print("you cheater!")
# LOOP TO ENTER ANOTHER GRADE
    if(input('\nWould you like to enter another grade? (y/n): ').lower() != 'y'):
        
        print('I don\'t blame you. Fuck them kids')
        break
