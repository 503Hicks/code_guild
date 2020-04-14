# Lab 14: Pick6

# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Steps

# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# Version 2

# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
# 100/20

import random
#CREATES LIST OF 6 RANDOM NUMBERS 1-99
def pick6():
    list1 = []
    for i in range(5):
        list1.append(random.randint(1,10))
    return list1
def get_ticket():
    list2 = []
    for i in range(5):
        list2.append(random.randint(1,10))
    return list2
def matching_nums(list1, list2):
    matches = 0
    for i in range(5):
        if list1[i] == list2[i]:
            matches +=1
    return matches
def payout(matches):
    winnings = 0
    if matches == 6:
        winnings = 25000000-2
    elif matches == 5:
        winnings = 1000000-2
    elif matches == 4:
        winnings = 50000-2
    elif matches == 3:
        winnings = 100-2
    elif matches == 2: 
        winnings = 7-2
    elif matches == 1:
        winnings = 4-2
    else:
        winnings = -2
    return winnings
def main():
    games = 0
    total_winnings = 0
    while games < 1000:
        win_num = pick6()
        user_num = get_ticket()
        # print(win_num)
        # print(user_num)
        print(f'your have {matching_nums(win_num, user_num)} matching numbers')
        # print(f' your payout is {payout(matching_nums(pick6(), get_ticket()))}')
        total_winnings += payout(matching_nums(win_num, user_num))
        games += 1
        roi = (total_winnings-200000)/200000
    print(f'Your total earnings is {total_winnings}')
    print(f'Your ROI is {roi}% ')
main()

