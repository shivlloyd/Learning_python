def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
print(factorial(15))


"""
This code defines a recursive function called `factorial` to 
calculate the factorial of a number. In the function, 
it first checks if the input `n` is equal to 0. If it is, it returns 1, 
as the factorial of 0 is defined as 1. Otherwise, it returns the product 
of `n` and the factorial of `n-1`. This is the recursive step where the 
function calls itself with a smaller input (`n-1`) 
until it reaches the base case (`n == 0`). 

Now, let's discuss how recursion works. Recursion is a programming technique 
where a function calls itself with smaller inputs to solve a problem. 
In the case of calculating factorial, each recursive call reduces the 
problem size until it reaches the base case, where the function returns a 
known value without making further recursive calls. 
Then, the function "unwinds" all the recursive calls, 
combining the results obtained at each step to produce the final result. 

In our code, when we call `factorial(5)`, it first calls `factorial(4)`, 
which in turn calls `factorial(3)`, and so on, until it reaches 
`factorial(0)`. At this point, it hits the base case and returns 1. 
Then, as the recursive calls unwind, each call multiplies its 
respective `n` with the result of the smaller factorial until we get the 
final result, which is the factorial of 5 (1 * 2 * 3 * 4 * 5 = 120). 
Therefore, the code prints `120`.
"""
