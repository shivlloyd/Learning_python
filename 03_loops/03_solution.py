number = int(input("Enter the number: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{number} X {i} = {number * i}")


"""
This code takes a number as input and prints its multiplication table 
up to 10, excluding the fifth iteration. It utilizes a for loop to
iterate from 1 to 10 inclusively. When the loop encounters 
the fifth iteration (i.e., when `i` equals 5), 
it skips to the next iteration using the `continue` statement. 
For all other iterations, it prints the multiplication expression 
and result using an f-string. This approach efficiently generates 
the desired multiplication table while excluding the fifth iteration.
"""
