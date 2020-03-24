# Lab 19: Blackjack Advice

# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

card_dict = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,}
card1 = input('What is your first card? ').upper()
card2 = input('What is your second card? ').upper()
card3 = input('What is your third card? ').upper()
user_sum = card_dict[card1] + card_dict[card2] + card_dict[card3]

if user_sum > 21:
    card_dict['A'] = 1
else:
    card_dict['A'] = 11

final_total = card_dict[card1] + card_dict[card2] + card_dict[card3]

print(f'{card_dict[card1]} + {card_dict[card2]} + {card_dict[card3]} = {final_total}')


if final_total <17:
    print('Hit')
elif final_total >= 17 and final_total < 21:
    print('Stay')
elif final_total > 21:
    print('Already Busted') 
