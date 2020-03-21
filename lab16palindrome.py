
import string



#FUNCTION FOR ANAGRAM CHECKER

def check_palindrome():
    palindrome_input = input("enter a word to see if it is a palindrome: ")
    if(palindrome_input==palindrome_input[::-1]):
      print(f'{palindrome_input} is a palindrome. ')
    else:
      print(f'{palindrome_input} is NOT a palindrome. ')
check_palindrome()


def check_anagram():
    anagram_input1 = input('Enter a word or phrase to check if anagram: ').lower()
    anagram_input2 = input('Enter a word or phrase to check if anagram: ').lower()
    sorted_input1 = sorted(anagram_input1)
    sorted_input2 = sorted(anagram_input2)
    if sorted_input1 == sorted_input2:
        print(f'{anagram_input1} and {anagram_input2} are anagrams. ')
    else:
        print(f'{anagram_input1} and {anagram_input2} are NOT anagrams. ')
check_anagram()
