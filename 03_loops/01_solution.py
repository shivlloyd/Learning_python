numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1

print(f"Toal count of positive numbers in list is {positive_number_count}")


"""
The for loop in this code iterates over each element in the `numbers` list one by one. 
For every element `num`, it checks if `num` is greater than 0, indicating a positive number.
If `num` meets this condition, the `positive_number_count` variable is incremented by 1. 
This process repeats for each element in the list until all elements have been checked. 
Once the loop completes, the total count of positive numbers found in the list is printed using an f-string. 
Essentially, the loop efficiently examines each element of the list and updates the count of positive numbers accordingly, 
providing a clear tally of positive integers within the list.
"""
