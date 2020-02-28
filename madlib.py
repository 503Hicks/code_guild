adj1 = input("Enter an adjective: ")
adj2 = input("Enter another adjective: ")
bird = input("Enter a type of bird: ")
room = input("Enter a room in a house: ")
verb1 = input("Enter a past tense verb: ")
verb2 = input("Enter a verb: ")
verb3 = input("Enter a verb inding in -ing: ")
verb4 = input("Enter a verb ending in -ing: ")
name = input("enter a relative's name: ")
liquid = input("Enter a liquid: ")
bodypart = input("Enter a part of the body; plural: ")
# noun1 = input("Enter a noun: ")
# noun2 = input("Enter a plural noun: ")
# noun3 = input("Enter a noun: ")

nouns = input("give three nounds seperated by a space")
nounds_list = nouns.split(', ')


# nounlist = []
# nounlist.append(nouns)



# for i in range(3):
#     nouns = input('enter three nouns')



print(f'It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs. I {verb1} down the stairs to see if I could help {verb2} the dinner. My mom said, "See if {name} needs a fresh {nouns[0]}." So I carried a tray of glasses full of {liquid} into the {verb3} room. When I got there, I couldn\'t believe my {bodypart}! There were {nouns[1]} {verb4} on the {nouns[2]}')