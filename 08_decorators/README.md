# What are decorators in python

In Python, decorators are a powerful way to modify the behavior of functions or methods. They allow you to add functionality to existing code without modifying it directly.

## Timing Function Execution

```python
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result

    return wrapper


@timer
def example_function(n):
    time.sleep(n)


example_function(2)
```

Now, let's focus on the `timer` decorator. This decorator measures the time it takes for a function to execute.

Here's how it works:

- The `timer` function itself is a decorator. It takes a function `func` as its argument.
- Inside `timer`, there's a nested function called `wrapper`. This `wrapper` function is what actually wraps around the original `func`.
- When you apply `@timer` to a function like `example_function`, what happens behind the scenes is that `example_function` gets replaced by `wrapper`. So, calling `example_function` actually calls `wrapper`.
- Inside `wrapper`, it records the start time using `time.time()` just before calling the original `func`.
- After calling `func`, it records the end time.
- Then, it calculates the difference between the start and end times to measure how long the function took to run.
- Finally, it prints out a message indicating the name of the function and the time it took to run, and returns whatever value `func` returned.

So, when you decorate a function with `@timer`, every time you call that function, it will print out how long it took to execute. This is a handy way to measure the performance of your functions without cluttering them with timing code.

## Debugging Function Calls

```python
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(
            f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_values}"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def hello():
    print("hello")


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


hello()
greet("Chai", greeting="Namaste ")
```

Now, let's focus on the `debug` decorator:

- The `debug` function is a decorator that takes another function `func` as its argument.
- Inside `debug`, there's a nested function named `wrapper`. This `wrapper` function wraps around the original `func`.
- When you decorate a function like `hello` or `greet` with `@debug`, it essentially replaces the original function with `wrapper`, so calling `hello()` or `greet()` actually calls `wrapper()`.
- Inside `wrapper`, it captures the arguments and keyword arguments passed to the function being decorated.
- It converts the arguments into a string format and prints out the function name along with the argument values and keyword argument values.
- After printing, it calls the original function `func` with the provided arguments and keyword arguments.
- The return value of `func` is then returned by `wrapper`.

So, when you decorate a function with `@debug`, every time you call that function, it will print out the function name along with the values of its arguments and keyword arguments. This can be incredibly useful for debugging and understanding how your functions are being called.

## Cache Return Values

```python
import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b


print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(5, 4))
```

Let's break down the code and understand how the `@cache` decorator works.

- The `cache` decorator function takes another function `func` as its argument.
- Inside `cache`, there's a dictionary `cache_value` initialized to an empty dictionary `{}`. This dictionary will hold the cached return values of the function.
- The `wrapper` function is nested inside `cache`. This function wraps around the original `func`.
- When you apply `@cache` to a function like `long_running_function`, it essentially replaces `long_running_function` with `wrapper`, so calling `long_running_function` actually calls `wrapper`.
- Inside `wrapper`, it first checks if the arguments passed (`args`) are already in the `cache_value`. If they are, it returns the cached result immediately without re-executing the function.
- If the arguments are not in the cache, it calls the original function `func` with the provided arguments, stores the result in the `cache_value` dictionary against the arguments as the key, and then returns the result.
- So, subsequent calls to `long_running_function` with the same arguments will return the cached result instead of re-executing the function.
- This caching mechanism helps to optimize performance, especially for functions with expensive computations or I/O operations.

In the provided example:

- The first call to `long_running_function(2, 3)` takes some time because it's not cached.
- The second call to `long_running_function(2, 3)` immediately returns the cached value without re-executing the function, hence it's faster.
- The third call to `long_running_function(5, 4)` also takes some time since it's a new set of arguments.
