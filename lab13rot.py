# lab 13 all version

# lab 15: ver 1 and 2
# lab 18 ver 1
# lab 19 do both version
# lab 20 do original

# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
# Version 2 (optional)

# Get user input 
import string


cap_letters = list(string.ascii_uppercase)
lower_letters = list(string.ascii_lowercase)
user_input = input("Enter your message to encrypt:  ")
rotation = int(input("Enter your rotation "))
input = list(user_input)
y = []

for i in input:
    if i in cap_letters:
        x = (cap_letters.index(i) + rotation) % 26
        y += cap_letters[x]
    elif i in lower_letters:
        x = (lower_letters.index(i) + rotation) % 26
        y += lower_letters[x]
    else:
        y.append(i)
y = "".join(y)
print(str(y))

