age = int(input("Enter your age: "))
day = input("Enter today's Day: ").lower()

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= 2
    print("You will get a $2 discount.")
    print(f"Your final ticket price is ${price}")
else:
    print("No discount for you.")
    print(f"Your final ticket price is ${price}")


"""
`lower()` converts the user input into lowercase and then assigns it to the `day` variable.

`price` will be 12 if age is greater or equal to 18, else it will be 8.

The `==` operator checks and returns `True` if both items are the same, `False` if not.

`price -= 2` decrements the price by 2 and then reassigns the new value to `price`.

`print(f"Your final ticket price is ${price}")` is known as formatted string literals.
It helps in printing the variable with a string.
It starts with `f` and encloses the variable in curly braces `{}`.
This enables easy and readable string formatting.
"""
