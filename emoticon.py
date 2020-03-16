#RANDOM EMOTICON GENERATOR

import random

eyes_list = [':', ';', '=',]
nose_list = ['-', '*', '^']
mouth_list = [']', '}', ')', '|', '(', '[', 'D', 'S']
#PRINTS 5 RANDOM EMOTIONS
i = 0
while i < 5:
    i += 1
    
    eyes = random.choice(eyes_list)
    nose = random.choice(nose_list)
    mouth = random.choice(mouth_list)

    print(eyes+nose+mouth)