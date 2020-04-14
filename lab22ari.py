ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

f = open('ion.txt.utf-8.txt', encoding='utf8')  # open the file
contents = f.read().lower()  # read the contents
print(contents)
f.close()  # close the file

# ari = 4.71(characters/words) + 0.5(words/sentences) - 21.43

def get_word_count():
    word_list = contents.split()#splits story into words
    word_count = int(len(word_list))
    print(word_count)
get_word_count()

def get_char_count():
    char_split = list(contents)
    char_count = int(len(char_split))
    print(char_count)
get_char_count()

def equation(w,c):
    div = get_word_count() / get_char_count()
    print(div)


# print(check)
# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts


# dict_count = {} #list of words to be counted in story
# for i in contents_list:
#     if i in dict_count:
#         dict_count[i] += 1
#     else:
#         dict_count[i] = 1