# Practice: Strings

# For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

# def add(a, b):
#     return a + b
# #print(add(5, 2))
# #print(add(8, 1))


# Problem 1

# Get a string from the user, print out another string, doubling every letter.


# string = input('enter something: ')
# check = 'abcde'
# some = check.join(check)


# s = "".join(list)
# for substring in list:
#     s += substringcd
# print(check)
# print(some)


user_input = int(input("enter a num between 1-99: "))

def words(user_input):
    units = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
    tens = ["Twenty","Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

 
    if n <=9:
        print(units[n])
    elif n >= 10 and n <= 19:
        return teens[n-10]
    elif n >= 20 and n <= 99:
        return tens[(n//10)-2] + " " + (units[n % 10] if n % 10 !=0 else "")