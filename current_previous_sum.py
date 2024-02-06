# Name:NOOR UL KARIM
# PNT SQA Batch-20 Online Batch
# Task: Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


for i in range(10):
    # Assigning i values to current and previous variables
    current = i
    previous = i - 1
    # making an if condition to make the starting previous value to be 0. This applies to first loop only
    if previous == -1:
        previous = 0

    print(
        "Current Number ",
        current,
        "Previous Number ",
        previous,
        "Sum: ",
        current + (previous),
    )
