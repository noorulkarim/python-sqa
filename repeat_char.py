# 1. Create a Python function that accepts a string. The function should return a string,
# with each character in the original string doubled. If you send the function “python” as
# a parameter, it should return “ppyytthhoonn” and if you send “123go!”, it should return
# “112233ggoo!!”

# Name: NOOR UL KARIM
# PNT SQA Batch-20


# In every for loop, each character is concataned twice to a new variable with (i+i) notation and then new variable is returned
def double_char(word):
    new_word = ""
    for i in word:
        new_word += i + i
    return new_word


# Take an input, pass it to function and print the return value
print(double_char(input("Give me a word or number:")))
