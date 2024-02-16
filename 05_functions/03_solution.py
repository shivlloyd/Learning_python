def multiply(p1, p2):
    return p1 * p2


print(multiply(6, 9))
print(multiply("G", 9))
print(multiply(7, "R"))


"""
multiply function takes two parameters, `p1` and `p2`. Inside the function, 
it performs the multiplication operation using the `*` operator 
and returns the result. The function is then called multiple times 
with different types of arguments: integers, strings, or a combination 
of both. Python supports the multiplication operation between strings 
and integers by repeating the string the specified number of times.

in python, the `*` operator has different behaviors depending on the 
types of the operands. When both operands are integers, 
it performs integer multiplication. However, when one operand is a 
string and the other is an integer, it repeats the string a number o
f times equal to the value of the integer. This behavior allows for 
flexible usage of the `*` operator, enabling operations like string 
repetition based on numeric values.
"""
