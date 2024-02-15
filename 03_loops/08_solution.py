number = int(input("Enter the Number: "))

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
else:
    is_prime = False

print(f"{number} is prime: {is_prime}")


"""
The code checks if a number is prime by iterating through numbers 
from 2 up to the number itself minus one. If the number is greater than 1, 
it checks if there are any factors other than 1 and itself. 
If it finds a factor, it sets a flag to indicate the number 
is not prime and breaks out of the loop. If the number is less than 
or equal to 1, it automatically sets the flag to indicate it's not prime. 
Finally, it prints whether the number is prime or not based on the value of the flag.
"""
