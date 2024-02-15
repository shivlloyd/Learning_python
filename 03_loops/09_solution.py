items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print(f"Duplicate item is {item}")
        break
    unique_item.add(item)


"""
The code aims to determine if all elements in a list are unique. 
It iterates through each item in the list. Within the loop, 
it checks if the current item is already present in a set called `unique_item`. 
If it is, it means a duplicate is found, and the code prints a message 
indicating the duplicate item. After checking each item, 
it adds the item to the `unique_item` set. This set ensures 
that duplicates are identified efficiently as sets do not allow duplicate 
elements. If a duplicate is found, the loop breaks to prevent further 
iterations, as the goal is to find the first duplicate.
"""
