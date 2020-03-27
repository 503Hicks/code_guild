# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

# Find a book on Project Gutenberg. Download it as a UTF-8 text file.

# Open the file.
# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", "$", "-","_","(",")", ]


f = open('ion.txt.utf-8.txt', encoding='utf8')  # open the file
contents = f.read().lower()  # read the contents


for i in punctuation:
    contents = contents.replace(i,"") #replaces punctuation.
    contents_list = contents.split(" ") #splits each item in list by whitespace
# print(contents)
# print(contents_list)

dict_count = {} #list of words to be counted in story
for i in contents_list:
    if i in dict_count:
        dict_count[i] += 1
    else:
        dict_count[i] = 1

# print(dict_count)

# word_dict is a dictionary where the key is the word and the value is the count
words = list(dict_count.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

