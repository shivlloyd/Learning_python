year = int(input("Enter the Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")


"""
The `and` operator returns True only if both of its conditions are True, otherwise it returns False.

The `or` operator returns True if at least one of its conditions is True.
If both conditions are false, it returns False.

To check what the remainder will be when two numbers are divided, we use the modulus operator `%`.

Comparison operators like `==` return True if both items are equal,
while `!=` returns True if both items are NOT equal.
"""
