# Name: NOOR UL KARIM
# PNT SQA Batch-20

# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "peoplentech" so you should display ‘p’, ‘o’, ‘l', ‘n', 'e', 'h'

word = input("Enter a word:")

for i in range(len(word)):
    if i % 2 == 0:
        print("'", word[i], "'", end=", ")
