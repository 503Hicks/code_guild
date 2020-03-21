
# import string
# ABC = list(string.ascii_uppercase)
# abc = list(string.ascii_lowercase)
# rotation = int(input("Enter your rotation "))
# user_input = input("Insert your code ")
# input = list(user_input)
# y = []
# for i in input:
#     if i in ABC:
#         x = (ABC.index(i) + rotation) % 26
#         y += ABC[x]
#     elif i in abc:
#         x = (abc.index(i) + rotation) % 26
#         y += abc[x]
#     else:
#         y.append(i)
# y = "".join(y)
# print(str(y))
# # 12-20 skip 16
# # version 18 only version 1

# import string

# def main():
    

#     user_num = int(input('Please enter a number between 1-999: '))
#     ones_dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
#     teens_dict = {10:'ten', 11:'eleven',12:'twelve',13:'thirteen',14:'fourteen', 15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen' }
#     tens_dict = {1: 'ten', 2:'twenty', 3: 'thirty', 4: 'fourty', 5:'fifty', 6:'sixty', 7:'seventy',8:'eighty',9:'ninety' } 
#     huns_dict = {1: 'one-hundred', 2:'two-hundred', 3:'three-hundred', 4: 'four-hundred', 5:'five-hundred', 6:'six-hundred', 7: 'seven-hundred', 8:'eight-hundred', 9:'nine-hundred'}

#     roman_ones = {0:'', 1:'I', 2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VII',9:'IX'}
#     roman_teens = {10:'X', 11:'XI',12:'XII',13:'XIII',14:'XIV',15:'XV',16:'XVI',17:'XVII',18:'XVIII',19:'XIX'}
#     roman_tens = {1:'X',2:'XX',3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
#     roman_huns = {1:'C',2:'CC',3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}

#     if 0 <= user_num and user_num <= 9:
#         print(ones_dict.get(user_num))
#         print(roman_ones.get(user_num))
#     elif 10 <= user_num and user_num <=19:
#         print(teens_dict.get(user_num))
#         print(roman_teens.get(user_num))
#     elif 20 <= user_num and user_num <=99:
#         print(f'{tens_dict.get(user_num//10)} {ones_dict.get(user_num%10)} ')
#         print(f'{roman_tens.get(user_num//10)}{roman_ones.get(user_num%10)}')
#     elif 100 <= user_num and user_num <=1000:
#         if (user_num//10)%10 == 1:
#             print(f'{huns_dict.get(user_num//100)} {teens_dict.get(user_num%100)}')
#             print(f'{roman_huns.get(user_num//100)}{roman_teens.get(user_num%100)}')
#         else:
#             print(f'{huns_dict.get(user_num//100)} {tens_dict.get((user_num//10)%10)} {ones_dict.get(user_num%10)}')
#             print(f'{roman_huns.get(user_num//100)}{roman_tens.get((user_num//10)%10)}{roman_ones.get(user_num%10)}')

# main()


# try:
#     f = open ('./points.txt')
#     contents = f.read()
#     print(contents)
# except(IOError, OSError) as e:
#     print(e)
# finally:
#     f.close()

import csv
import matplotlib.pyplot as plt 

with open('./points.py') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    x = []
    y = []

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            x.append(row[0])
            y.append(row[1])
            line_count +=1

plt.scatter(x.y)
ply.show()


