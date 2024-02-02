# 3. Write a function in Python that accepts a credit card number. It should return a string where all
# the characters are hidden with an asterisk except the last four. For example, if the function gets
# sent “4535678890878989”, then it should return “**8989”

# Name: NOOR UL KARIM
# PNT SQA Batch-20


# Running a while loop from position 12th character till 16th character and concatanate it to predefined 12 "*" and return the new variable
def last_four_digit(number):
    hidden_num = "**************"
    i = 12
    while i < len(number):
        hidden_num += number[i]
        i += 1
    return hidden_num


# Take a credit card input to pass it to function and get return value with asterisks
print(last_four_digit(input("Credit Card Number: ")))
