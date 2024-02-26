file = open("yotube.txt", "w")

try:
    file.write("chai aur code")
finally:
    file.close()

with open("yotube.txt", "w") as file:
    file.write("Chai aur python")
