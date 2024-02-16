def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Superman", power="Flying")
print_kwargs(name="Green Arrow")
print_kwargs(power="Running", name="Flash")
print_kwargs(name="Batman", power="Rich", enemy="Joker")


"""
This code defines a function named `print_kwargs` that accepts 
any number of keyword arguments using the `**kwargs` syntax. 
The `**kwargs` syntax allows the function to accept 
an arbitrary number of keyword arguments, which are then collected 
into a dictionary called `kwargs`. Inside the function, 
it iterates through each key-value pair in the `kwargs` dictionary 
using the `.items()` method. For each pair, it prints the key followed 
by a colon and then the corresponding value, formatting it as `"key: value"`. 
When you call `print_kwargs` with various keyword arguments like `name="Superman", power="Flying"`
it prints out each keyword argument in the specified format.
"""
