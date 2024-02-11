distance = int(input("Enter the distance: "))

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
elif distance <= 100:
    transport = "Car"
elif distance <= 1000:
    transport = "Train"
else:
    transport = "Plain"

print(f"AI recommends you the transport of {transport} to travel {distance} Km.")
