from random import choice

# a_list = ['a', 'b', 'c', 'd']

# print(choice(a_list))

#import ransom
#random.choice


def choose(a_list):
    rand_item = choice(a_list)
    a_list.remove(rand_item)
    return rand_item

def main():
    user_input = []

    promts = [
        '\Give me an anonym for \'data\':',
        'Give me a noune: ',
        'Tell me an adjectieve: ',
        'a type of animal (plural): '
        'some sciency thing: ',
        'another sciency thing: ',
        'sciency adjective: ',
    ]
    while True:
        for prompt in prompts:
            user_input.append(input(prompt))
        
        madlib =f'\n{choose(user_input)} scientist job description: \
            \nSeeking a {choose(user_input)} engeneer, able to work on {choose(user_input)} projects with a team of {choose(user_input)}. \
            \nKey responsibilities: \
            \n- extract patterns from {choose(user_input)}\
            \n - Optimize {choose(user_input)}\
            \n - Transform{choose(user_input)} into {choose(user_input)} material/'

    print(madlib)

    if(input('\nWould you like to make another (y/n): ').lower() != 'y'):
        print('I don\'t blame you. I dont like Mad libs either')
        break

main()