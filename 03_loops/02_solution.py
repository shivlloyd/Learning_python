n = int(input("Enter the number: "))

sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print(f"Sum of even numbers upto {n} is {sum_even}")


"""
This code prompts the user to input a number (`n`) and initializes a variable `sum_even` 
to store the sum of even numbers up to `n`. 
It then utilizes a for loop with the `range()` function 
to iterate from 1 to `n` (inclusive). Within the loop, 
it checks if each number (`i`) is even by using the modulo operator `%` 
to check if the remainder of `i` divided by 2 equals 0. If `i` is indeed even, 
it adds the value of `i` to the `sum_even` variable. Once the loop completes, 
the code prints out the sum of even numbers up to `n` using an f-string. 
Essentially, this code efficiently calculates the sum of even numbers 
within the specified range provided by the user, providing a clear result at the end.
"""
