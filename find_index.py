# Name: NOOR UL KARIM | PNT SQA Batch-20
# Python Task-4 Problem-2:
# Write a python function that takes a list and a target element and returns the index of the target element in the list, or -1 if it is not found. This exercise demonstrates the concept of linear search, which involves iterating through a list to find a specific element.
# Example Input: numbers = [2, 4, 6, 8, 10] target = 6
# Example Output: Index: 2


def find_index_position(num_list, target_element):
    try:
        return num_list.index(target_element)
    except ValueError:
        return -1


num_list = [2, 4, 6, 8, 10]
target_element = 10
print(find_index_position(num_list, target_element))
