#version 1 & 2

while True:
    # operation = input("What is the operation you'd like to perform? '+,-,*,/' ").lower()
    
    # if operation == 'done':
    #     break

    # num1 = float(input("What is the first number? "))
    # num2 = float(input("What is the second number? "))
    
    # if operation == '+':
    #     print(add())
    # elif operation == '-':
    #     print(subtract())
    # elif operation == '*':
    #     print(multiply())
    # elif operation == '/':
    #     print(divide())
    # else:
    #     print("Try again using a '+', '-', '*', or '/' symbol\nOr press 'Done' to quit. ")
    

    
# Version 3:
    calc = eval(input("Enter a calculation: "))
    if calc == 'done':
        break
    else:
        print(calc)

