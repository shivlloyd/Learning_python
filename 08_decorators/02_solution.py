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
