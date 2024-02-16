import math


def circle_stats(radius):
    area = round(math.pi * radius**2, 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference


a, c = circle_stats(5)

print(f"Area: {a}, Circumference: {c}")


"""
This Python code defines a function called `circle_stats` that calculates 
both the area and circumference of a circle given its radius. 
It utilizes the `math` module to access the value of pi (`math.pi`). 
Inside the function, it computes the area using the formula `pi * radius squared` 
and the circumference using the formula `2 * pi * radius`. The `round()` 
function is then used to round the calculated values to two decimal places. 
The function returns both the area and circumference as a tuple.

Outside the function, the `circle_stats` function is called with a radius 
of `5`, and the returned values are unpacked into variables `a` and `c`. 
Finally, these values are printed using a formatted string to display 
the area and circumference with appropriate labels. 
"""
