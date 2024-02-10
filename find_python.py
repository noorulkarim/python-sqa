# Name: NOOR UL KARIM
# PNT SQA Batch-20

# Write a program to find how many times substring " Python" appears in the given string.
# Input:
# str = "Python is a modern programming language. I like to code in Python."
# Output: Python appeared 2 times.

sentence = input("Enter a sentence:")
count = sentence.lower().count("python")

if count != 0:
    print("Python appeared ", count, " times")
