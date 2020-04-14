import random



# For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

# def add(a, b):
#     return a + b
# #print(add(5, 2))
# #print(add(8, 1))


# Problem 1

# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

# def random_element(a):
#     ...
def random_element():
    
fruits = ['apples', 'bananas', 'pears']
print(random.choice(fruits))


# random_element(fruits) could return 'apples', 'bananas' or 'pears'