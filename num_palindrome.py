# Name:NOOR UL KARIM
# PNT SQA Batch-20 Online Batch
# Write a program to take a number as input from the user and show whether it is palindrome or not


def isPalindrome(number):
    num = []
    rev_num = []
    count = 0
    length = str(number)

    for i in length:
        num.append(i)
        rev_num.insert(0, i)

    for i in range(len(length)):
        if num[i] == rev_num[i]:
            count += 1

    if count == len(length):
        return print("The number", number, "is a palindrome")
    else:
        return print("the number", number, "is NOT a palindrome")


number = int(input("Tell me some numbers: "))
isPalindrome(number)
