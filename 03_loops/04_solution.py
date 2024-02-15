input_str = input("Enter the String to reverse: ")

reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print(reversed_str)


"""
This code allows the user to input a string (`input_str`). 
It then initializes an empty string `reversed_str` to store the 
reversed version of the input string. Utilizing a `for` loop, 
the code iterates over each character (`char`) in the `input_str`. 
For each character, it prepends (`char + reversed_str`) the current 
character to the existing `reversed_str`. This effectively reverses 
the order of characters in the string. After all characters have been 
processed in the loop, the code prints out the `reversed_str`, 
which now contains the reversed version of the input string. 
"""
