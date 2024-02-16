# Name: NOOR UL KARIM | PNT SQA Batch-20
# Python Task-4 Problem-1:
# Write a python program (function) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Examle Input: ["John", "Robin", "Bob", "John", "Alice", "Robin"]
# Example Output:["John", "Robin", "Bob", "Alice"]


def remove_duplicates(words):
    distinct_list = []
    for i in words:
        if distinct_list.count(i) == 1:
            continue
        distinct_list.append(i)
    return distinct_list


words = ["John", "Robin", "Bob", "John", "Alice", "Robin", "Bob"]
print(remove_duplicates(words))
