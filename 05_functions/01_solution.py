def square(number):
    return number**2


result = square(4)
print(result)


"""
The given code defines a function called `square` which takes 
a parameter `number` and returns its square using the exponentiation 
operator (`**`). The function is then called with an argument of `4`, 
and the result is stored in a variable named `result`, which is then printed. 

In Python, defining a function involves using the `def` keyword 
followed by the function name and its parameters. It's important 
for functions to return a value because it allows them 
to provide a result that can be used in other parts of the program. 
If we print `square(4)` directly without assigning it to a variable, 
the result will still be printed, but we won't be able to reuse it later in the code.

Functions encapsulate reusable blocks of code, 
promoting modularity and readability in programs. 
They allow for easier debugging, testing, 
and maintenance by isolating specific tasks into separate units.
"""
