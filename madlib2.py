import random

madlib_again = "yes"

while madlib_again == "yes":
    nouns = input("Enter 3 nouns seperated by commas: ")
    nouns_list = nouns.split(", ")
    nounshuffle = random.shuffle(nouns_list)

    verbs = input("Enter 2 verbs seperated by a comma: ")
    verbs_list = verbs.split(", ")
    verbshuffle = random.shuffle(verbs_list)

    adjs = input("Enter 2 adjectives seperated by a comma:")
    adjs_list = adjs.split(", ")
    adjshuffle = random.shuffle(adjs_list)

    color1 = input("Enter a color: ")
    food = input("Enter a food: ")
    number = input("Enter a number: ")
    
    # adj1 = input("Enter an adjective: ")
    # adj2 = input("Enter another adjective: ")
    # verb1 = input("Enter a verb: ")
    # verb2 = input("Enter another verb: ")
    # noun1 = input("Enter a noun: ")
    # noun2 = input("Enter another noun: ")
    # noun3 = input("Enter another another noun: ")


    print(f"Select the type of bread you want to use. Many prefer the taste of {color1} bread, while others prefer {nouns_list[0]} bread because it is healthy. Choose a flavor of Jam/Jelly. I personally prefer {food} jam, but you can use whatever you want. Choose a type of penut butter - either {adjs_list[0]} or {adjs_list[1]}. Take out {number} slices of bread. use a {nouns_list[1]} to {verbs_list[0]} the jam all over one of the pieces of bread. Now {verbs_list[1]} the penut butter on the other piece of bread. Put them together, and you have a PB&J {nouns_list[2]}." )

    madlib_again = input("Would you like to play your madlib again?(yes or no) ").lower()
else:
    print("Goodbye!")