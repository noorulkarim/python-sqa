# Name:NOOR UL KARIM
# PNT SQA Batch-20 Online Batch
# Exercise: Write a program to take a string as input from the user and show whether it is palindrome or not


def isPalindrome(word):
    # Declaring empty list to store string characters and count variable to store counts
    string = []
    rev_string = []
    count = 0
    # Looping through for loop to append characters in the end for string list
    # and using insert() for rev_string to insert characters in the beginning of the list
    for i in word:
        string.append(i)
        rev_string.insert(0, i)
    # Looping again by the length of the word, example: hello will make it go 5 times,
    # if both list values are same in each indices position from both direction, increment count value by one
    for i in range(len(word)):
        if string[i] == rev_string[i]:
            count += 1
    # if count value is equal to the length of the word, the input word is a palindrome
    if count == len(word):
        return print("The word", word, "is a palindrome")
    else:
        return print("the word", word, "is NOT a palindrome")


word = input("Tell me a word:")
isPalindrome(word)
