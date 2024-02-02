# 2. Create a function in Python that accepts two parameters. The first should be the full price
# of an item as an integer. The second should be the discount percentage as an integer. The function
# should return the price of the item after the discount has been applied. For example, if the price
# is 100 and the discount is 20, the function should return 80.

# Name: NOOR UL KARIM
# PNT SQA Batch-20


def price_discount(price, discount):
    return price * ((100 - discount) / 100)


price = int(input("Price: $ "))
discount = int(input("Discount Rate:"))

print("The discounted rate is $", price_discount(price, discount))
