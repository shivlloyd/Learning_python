order_size = input("Enter the coffee size (small, medium, or large): ").capitalize()
extra_shot = input("You want extra shot? (Yes/No): ")
extra_shot = extra_shot.lower() == "yes"

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)

"""
In the line `extra_shot = extra_shot.lower() == "yes"`, we are converting "yes" into the boolean `True` value.
If the input is "no", then `extra_shot` will become the boolean `False`.

In the line `if extra_shot:`, this `if` statement will evaluate to `True`,
and execute only if `extra_shot` is `True`.

In the line `order_size + " coffee with an extra shot"`, this is called string concatenation.
The `order_size` variable has a string value,
and it's being concatenated with another string to form a meaningful sentence.
"""
