def greet(name="User"):
    return "Hello, " + name + " !"


print(greet("Shivam"))

"""
here we defined a function called `greet` which takes one parameter `name` 
with a default value of "User". Inside the function, 
it constructs a greeting message by concatenating the string "Hello, " 
with the provided `name` parameter (or the default "User" 
if no name is provided), followed by an exclamation mark. 
Finally, it returns this greeting message. When you call the function 
`greet("Shivam")`, it will replace the default "User" with "Shivam" and print "Hello, Shivam!".
"""
