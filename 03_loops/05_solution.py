input_str = input("Enter the string: ")

for char in input_str:
    if input_str.count(char) == 1:
        print(f"first non-repeated character is '{char}'")
        break

"""
It begins by prompting the user to input a string, 
which is stored in the variable `input_str`. 
Then, it employs a for loop to iterate over each character (`char`) 
in the input string. Within the loop, it utilizes the `count()` 
method to determine the number of occurrences of the current character in the input string. 
If the count is equal to 1, it implies that the character 
is not repeated in the string. In this case, 
it prints a message indicating that the first non-repeated character has 
been found, along with the character itself. The `break` statement ensures 
that the loop terminates after finding the first non-repeated character, 
as it's not necessary to continue searching once the desired character is found. 
Thus, the code efficiently identifies and reports the first non-repeated character in the given string.
"""
