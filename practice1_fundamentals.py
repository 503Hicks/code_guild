# Problem 1

# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    return a%2 == 0

print(is_even(3))

# Problem 2

# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def pos_and_neg(a, b):
    return (a*b) < 0

print(pos_and_neg(2,-4))


# Problem 3

# Write a function that returns True if a number within 10 of 100.


def near_100(num):
    return 10 <= num <= 100

print(near_100(15))


# Problem 4

# Write a function that returns the maximum of 3 parameters.

def max_of_3(a,b,c):
    return max(a,b,c)

print(max_of_3(14,9,7))



# Problem 5

# Print out the powers of 2 from 2^0 to 2^20


# def power_of_2

def power_of_2(a):
    for i in range(20):
        print(a**i)
    
power_of_2(2)