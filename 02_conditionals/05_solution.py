weather = input("Enter the current weather: ").capitalize()

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":
    activity = "Build a snowman"

print(f"You can {activity}")


"""
`capitalize()` converts the first letter of each user input string into uppercase.
"""
