pet_species = input("Enter your pet species: ").lower()
pet_age = int(input(f"Enter your {pet_species}'s age (in years): "))

if pet_species == "dog":
    if pet_age < 2:
        print(f"Puppy Food is recommended for your {pet_age} years old {pet_species}")
    elif pet_age >= 2:
        print(
            f"Adult Dog Food is recommended for your {pet_age} years old {pet_species}"
        )
elif pet_species == "cat":
    if pet_age < 5:
        print(
            f"Junior cat food is recommended for your {pet_age} years old {pet_species}"
        )
    elif pet_age >= 5:
        print(
            f"Senior cat food is recommended for your {pet_age} years old {pet_species}"
        )
else:
    print(f"We dont have any pet food for {pet_species}")
