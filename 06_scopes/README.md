## Scopes and closure in python

```python
username = "ChaiAurCode"

def func():
    username = "chai"
    print(username) // "chai"

print(username) // "ChaiAurCode"
func()
```

In Python, the term "scope" refers to the region of a program where a particular variable can be accessed or referenced. It determines the visibility and accessibility of variables within a program. Understanding scope is crucial for writing code that behaves as expected and for avoiding unintended consequences such as variable name clashes or unexpected variable modifications.

In this Python code snippet, we have a global variable `username` assigned the value `"ChaiAurCode"`. Then, we define a function `func()` which contains a local variable `username` assigned the value `"chai"`. When the function `func()` is called, it prints the value of the local variable `username`, which is `"chai"`. However, outside the function, when we print `username`, it refers to the global variable `username`, hence it prints `"ChaiAurCode"`. This happens because within the function, Python looks for the variable `username` first in the local scope, and only if it's not found there does it look in the global scope. Since the local variable `username` exists within the function, it takes precedence over the global variable with the same name. Therefore, the output of the code will be `"ChaiAurCode"` followed by `"chai"`. This demonstrates the concept of variable scope in Python, where the local variable within a function can shadow (or override) a global variable with the same name, but only within the scope of that function.

```python
x = 99

def func2(y):
    z = x + y
    return z

result = func2(1)
print(result) // prints 100
```

here we have a global variable `x` assigned the value `99`. Then, we define a function `func2(y)` which takes a parameter `y`. Inside the function, a local variable `z` is defined and assigned the value of `x` (which is a global variable) plus the parameter `y`. The function returns the value of `z`. When the function `func2()` is called with the argument `1`, `z` is calculated as `99 + 1`, resulting in `100`. This value is then assigned to the variable `result`. Finally, `result` is printed, which outputs `100`. This code illustrates how Python handles variable scope: the function can access global variables like `x` within its scope, allowing it to perform operations with both global and local variables. Thus, `func2()` can access `x` even though it's defined outside the function, demonstrating the concept of variable scoping in Python.

```python
x = 99

def func3():
    global x
    x = 16

func3()
print(x)
```

here we have a global variable `x` assigned the value `99`. Inside the function `func3()`, we use the `global` keyword to explicitly declare that we want to modify the global variable `x`. Then, we reassign the value of `x` to `16`. When the function `func3()` is called, it modifies the global variable `x` to `16`. Consequently, when we print `x` after calling `func3()`, it outputs `16`, indicating that the value of the global variable `x` has been successfully changed by the function `func3()`. This code demonstrates the usage of the `global` keyword in Python, allowing functions to modify variables defined in the global scope. It highlights the concept of variable scoping in Python, where the `global` keyword enables access to and modification of global variables from within a function's local scope.

```python
x=99

def f1():
    x = 88
    def f2():
        print(x)

    f2()

f1()
```

here we have a global variable `x` assigned the value `99`. Inside the function `f1()`, there's a local variable `x` assigned the value `88`. Within `f1()`, we also have another nested function `f2()`. When `f1()` is called, it invokes `f2()` internally. Now, `f2()` doesn't have its own local variable `x`, so it looks for `x` in its enclosing scope, which is `f1()`. It finds `x` there and prints its value, which is `88`. This output may seem unexpected because one might expect `f2()` to print the global variable `x`, which is `99`. However, Python's scoping rules dictate that when a variable is referenced within a function, Python first looks for it in the local scope, then in enclosing scopes (if it's a nested function), and finally in the global scope. Therefore, `f2()` prints the value of `x` from its nearest enclosing scope, which is `f1()`. This showcases the concept of variable scoping and nested functions in Python.

```python
def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()

myResult()
```

now here we have a function `f1()` that defines a local variable `x` with the value `88`, and then it defines another nested function `f2()`, which prints the value of `x`. The key point here is that `f2()` is defined within the scope of `f1()`, meaning it has access to the variables of its enclosing function. When `f1()` is called, it returns the function `f2()` as its result. This is known as a closure, where a function retains access to variables from its enclosing scope even after that scope has finished executing. So, when we call `myResult()`, which is assigned the function returned by `f1()`, it executes `f2()`, and because `f2()` still has access to the variable `x` from the scope of `f1()`, it prints the value `88`. This demonstrates how closures work in Python, allowing functions to retain access to variables from their enclosing scopes even after those scopes have finished executing.

```python
def chaicoder(num):
    def actual(x):
        return x**num

    return actual


f = chaicoder(2)
g = chaicoder(3)
print(f(3))
print(g(4))
```

here we define a function `chaicoder(num)` that takes a parameter `num`. Inside `chaicoder()`, we define another nested function `actual(x)` that takes a parameter `x` and returns `x` raised to the power of `num`. This inner function `actual(x)` captures the value of `num` from its enclosing scope, forming a closure. When `chaicoder()` is called with an argument, it returns the inner function `actual()`, customized with the value of `num` passed during its invocation. We then assign the results of `chaicoder(2)` and `chaicoder(3)` to `f` and `g` respectively. These assignments effectively create two different functions, `f(x)` and `g(x)`, each with their own independent closure. When we call `f(3)`, it calculates `3` raised to the power of `2`, resulting in `9`. Similarly, `g(4)` calculates `4` raised to the power of `3`, resulting in `64`. This demonstrates the concept of closures in Python, where inner functions retain access to variables from their enclosing scopes, even after those scopes have finished executing, allowing for customizable behavior based on the values captured during function creation.
