# Lab 10: Average Numbers

# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

# The code below hows how to loop through an array, and prints the elements one at a time.

# nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
# Version 2

# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

# nums = []
# nums.append(5)
# print(nums)
# Below is an example input/output:

# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4


#AVERAGE NUMBER

#USERS LIST
user_list = []

while True:
    #USERS INPUT OF NUMBERS TO BE AVERAGED
    user_input = input('Enter a number or enter "done" when finished. ').lower()
    if user_input == 'done':
        break
    user_list.append(int(user_input))
#USERS AVERAGE
list_average = sum(user_list)/len(user_list)
#OUTPUT OF USERS LIST & AVERAGE OF SUM IN LIST
print(user_list)
print(f'Your average is {list_average}.')

