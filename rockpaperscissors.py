import random
import string


choices = ['rock', 'paper', 'scissors']
# play_again = 'yes'


while True:


    user_choice = input("Rock, paper, scissors?").lower()
    comp_choice = random.choice(choices)


    print(f"{user_choice} vs {comp_choice}")


    if user_choice == comp_choice:
        print('Its a tie!')
    elif user_choice == 'rock' and comp_choice == 'paper':
        print('Paper covers rock... YOU LOSE!!')
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print('Rock smashes scissors... YOU WIN!!!')
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('Paper covers rock... YOU WIN!!!')
    elif user_choice == 'paper' and comp_choice == 'scissors':
        print('Scissors cuts paper... YOU LOSE!!!')
    elif user_choice == 'scissors' and comp_choice == 'rock':
        print('Rock smashes scissors... YOU LOSE!!!')
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print('Scissors cuts paper... YOU WIN!!!')

    play_again = input('Would you like to play again?').lower()
    if play_again != 'yes':
        print("later loser!")
        break

  
