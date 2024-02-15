number = int(input("Enter the Number: "))

factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"Factorial is {factorial}")


"""
It first prompts the user to input a number, which is stored in the 
variable `number`. Then, it initializes a variable called `factorial` to 1, 
which will hold the final factorial value. The while loop continues 
as long as `number` is greater than 0. Within each iteration of the loop, 
it multiplies `factorial` by the current value of `number`, 
effectively accumulating the factorial value. After the multiplication, 
it decrements `number` by 1 to progress towards computing the factorial. 
This process continues until `number` becomes 0, at which point the loop 
terminates. Finally, it prints out the computed factorial value. 
"""
