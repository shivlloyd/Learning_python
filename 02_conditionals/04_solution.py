fruit = input("Enter the fruit name: ")
color = input("Enter the fruit color: ")

if fruit == "banana":
    if color == "green":
        print(f"Your {fruit} is Unripe")
    elif color == "yellow":
        print(f"Your {fruit} is Ripe")
    elif color == "brown":
        print(f"Your {fruit} is OverRipe")
else:
    print("We have the Ripeness information of only Banana.")


"""
First, we'll check the fruit you are having, and then we will check its color to determine it's ripeness.

What we did here is called nested if statements, 
which means a conditional statement inside another conditional statement.
"""
