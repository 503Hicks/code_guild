# f = open('filename.txt')  # open the file
# contents = f.read()  # read the contents
# print(contents)
# f.close()  # close the file
import csv 


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

# contacts= [{'name':'matthew', 'favorite fruit': 'blackberries', 'favorite color':'orange',},
# {'name':'deaudre', 'favorite fruit': 'bananas', 'favorite color': 'green'}

