def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)


print(sum_all(1, 2, 3))

"""
This code defines a function named `sum_all` that accepts a variable 
number of arguments using the `*args` syntax. The `*args` syntax allows 
the function to accept any number of positional arguments, which are then 
collected into a tuple called `args`. Inside the function, 
it first prints out all the arguments passed to it. Then, 
it iterates through each argument in the tuple `args`, 
doubling each argument's value and printing it. Finally, 
it returns the sum of all the arguments using the `sum()` function, 
which calculates the total sum of all the elements in the `args` tuple. 
When you call `sum_all(1, 2, 3)`, it prints each argument (1, 2, 3), 
doubles each argument (2, 4, 6), and returns their sum, which is `1 + 2 + 3 = 6`. 
So, the output of `print(sum_all(1, 2, 3))` is `6`.
"""
