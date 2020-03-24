



cc_list
cc_input = int(input('Enter CC number: '))

print(cc_num)



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