password = input("Enter your Password: ")
password_length = len(password)

if password_length < 6:
    strength = "Weak"
elif password_length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Your password strength is {strength}")

"""
`len()` returns the number of characters in the `password` variable as an integer data type.
After that, we can check which category the user's password falls under.
"""
