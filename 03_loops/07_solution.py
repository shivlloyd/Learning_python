while True:
    number = int(input("Enter value b/W 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number try again")


"""
It uses a while loop with an indefinite condition. Within each iteration, 
it checks if the input number falls within the specified range. 
If it does, it prints "Thanks" and exits the loop. Otherwise, 
it notifies the user of an invalid input and continues looping until 
a valid input is provided. This approach ensures that only 
valid numbers within the desired range are accepted.
"""
