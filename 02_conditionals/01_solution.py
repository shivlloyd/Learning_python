age = int(input("Give me your age: "))

if age < 13:
    print("Your a Child")
elif age < 20:
    print("You are a Teenager")
elif age < 60:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")


"""
`input()` waits for the user to provide input and then assigns that value to the variable `age`.
`int()` converts the input to an integer format because by default `input()` returns the value as a string.

`if` and `elif` check if the statement is true; if so, they proceed with the operations, otherwise, they skip and the program moves forward.
`else` gets executed if all `if` and `elif` conditions fail.

Indentations in Python are very important as they determine which block of code is under which conditional statement.
"""
