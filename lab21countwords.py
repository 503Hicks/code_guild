# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

# Find a book on Project Gutenberg. Download it as a UTF-8 text file.

# Open the file.
# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", "$", "-","_","(",")", ]


f = open('ion.txt.utf-8.txt')  # open the file
contents = f.read().lower()  # read the contents
for i in punctuation:
    contents = contents.replace(i,"")
    contents_list = contents.split(" ")
# print(contents)
print(contents_list)





# book = input("Enter a string:").lower()
# #REPLACES PUNCTUATION
# for i in punctuation:
#     book = book.replace(i,"")
# print(book)
# #SPLITS BOOOK INTO LIST
# book = book.split()
# print(book)