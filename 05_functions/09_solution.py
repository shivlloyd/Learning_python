def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)


"""
This code defines a generator function called `even_generator` that yields 
even numbers up to a specified limit. Inside the function, 
it utilizes a `for` loop with the `range` function to iterate through 
even numbers starting from 2 up to the specified `limit`, 
incrementing by 2 in each step to ensure only even numbers are generated. 
Instead of returning these numbers like a regular function, it uses the `yield` keyword. 

Now, let's delve into how `yield` works and manages memory in Python. 
When a function encounters a `yield` statement, it temporarily suspends 
its execution and returns the yielded value. However, it retains its state, 
allowing it to resume execution from where it left off 
the next time it's called. This characteristic makes generators 
memory-efficient because they don't store all values in memory at once. 
Instead, they generate values on-the-fly as they're needed, 
thus reducing memory usage, especially when dealing with large datasets. 

In our code, `even_generator` yields even numbers one at a time, 
avoiding the need to store all even numbers up to the limit in memory simultaneously. 

Finally, the `for` loop outside the function iterates over the values 
yielded by `even_generator(10)`, printing each even number generated by the function. 
When you run this code, it prints even numbers from 2 to 10 inclusively.
"""
