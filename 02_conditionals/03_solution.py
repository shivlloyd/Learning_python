name = input("enter student's name: ")
score = int(input("Enter the Score: "))

if score >= 101 or score < 0:
    print("Please verify your grade again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{name} scored Grade: {grade}")


"""
In the line `if score >= 101 or score < 0:`, it will evaluate to True if either one of the statements `score >= 101` or `score < 0` is True.
Consequently, the entire `if` statement will become True, and the code inside the `if` block will execute.

`exit()` terminates the Python code once it is encountered.
"""
