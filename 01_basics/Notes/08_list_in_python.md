## List in Python

```python
>>> tea_varities = ["Black", "Green", "Oolong", "White"]
>>> tea_varities
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varities[0])
Black
>>> print(tea_varities[2])
Oolong
>>> print(tea_varities[-1])
White
>>> print(tea_varities[1:3])
['Green', 'Oolong']
>>> print(tea_varities[:2])
['Black', 'Green']
>>> print(tea_varities[2:])
['Oolong', 'White']
>>> tea_varities[3]
'White'
```

We can perform indexing and slicing in lists as well.

Indexing starts from 0 up to the length of the list minus 1.

```python
>>> tea_varities[3] = "Herbal"
>>> print(tea_varities)
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varities[1:2]
['Green']
>>> tea_varities[1:2] = ["Lemon"]
>>> tea_varities
['Black', 'Lemon', 'Oolong', 'Herbal']
>>> tea_varities[1:3]
['Lemon', 'Oolong']
>>> tea_varities[1:3] = ["green", "Masala"]
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
```

We can assign a new element to a specific list index. However, if we want to change multiple items at a specific index range, we can do something like this:

```python
tea_varieties[1:3] = ["green", "Masala"]
```

This sets the new items in the index range starting from 1 up to (3-1), resulting in `['Black', 'green', 'Masala', 'Herbal']`.

```python
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
>>> tea_varities[1:1]
[]
>>> tea_varities[1:1] = ['test', 'test']
>>> tea_varities
['Black', 'test', 'test', 'green', 'Masala', 'Herbal']
>>> tea_varities[1:2]
['test']
>>> tea_varities[1:3]
['test', 'test']
>>> tea_varities[1:3] = []
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
```

`tea_varieties[1:1]` shows an empty array because indexing starts from 1 and ends at (1-1), resulting in an empty range.

`tea_varieties[1:1] = ['test', 'test']` inserts two new items at the starting index 1.

`tea_varieties[1:3] = []` removes the two items from indexes 1 and 2 by specifying to insert 'nothing' in those indexes.

```python
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
>>> for tea in tea_varities:
...     print(tea)
...
Black
green
Masala
Herbal
>>> for tea in tea_varities:
...     print(tea, end="-")
...
Black-green-Masala-Herbal->>>
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong tea")
```

A `for` loop iterates through the `tea_varieties` list and assigns each value to the variable `tea`. For each iteration, it performs the print operation.

We can choose how to print the items using `print(tea, end="-")`, which puts "-" after the end of each value.

`if` conditions can be used to check whether an item is present in the list or not and give instructions accordingly. For example:

```python
if "Oolong" in tea_varieties:
    print("I have Oolong tea")
```

Here, if "Oolong" is present in the list, then it will print "I have Oolong tea". However, if "Oolong" is not in the list, it won't print anything.

```python
>>> tea_varities.append("Oolong")
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal', 'Oolong']
>>> if "Oolong" in tea_varities:
...     print("I have Oolong Tea")
...
I have Oolong Tea
>>> tea_varities.pop()
'Oolong'
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
>>> tea_varities.remove("green")
>>> tea_varities
['Black', 'Masala', 'Herbal']
>>> tea_varities.insert(1, "green")
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
```

`append()` adds a new item at the end of the list.

So, using `append()`, we added the "Oolong" tea to the list. Now, if `"Oolong" in tea_varieties`,  
it will print "I have Oolong Tea".

`pop()` by default removes the last item from the list and displays which item it has removed. Here, it removed "Oolong" because it was the last item in the list.

`remove()` can also delete a specific item, so we have to mention that specific item which we want to remove, and it doesn't return the value it deleted.

`insert(1, "green")` adds the item "green" at the specific index '1' and shifts the previous items present from index 1 to the right.

```python
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
>>> tea_varities_copy = tea_varities
>>> tea_varities_copy = tea_varities.copy()
>>> tea_varities_copy
['Black', 'green', 'Masala', 'Herbal']
>>> tea_varities_copy.append("Lemon")
>>> tea_varities
['Black', 'green', 'Masala', 'Herbal']
>>> tea_varities_copy
['Black', 'green', 'Masala', 'Herbal', 'Lemon']
```

`tea_varieties_copy = tea_varieties` gives a reference to the same memory location of the list `tea_varieties`.

`tea_varieties_copy = tea_varieties.copy()` generates another list with the same values as `tea_varieties` and then passes the reference of the new list to `tea_varieties_copy`.

That's why when "Lemon" was added to `tea_varieties_copy`, it didn't change `tea_varieties`.

```python
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> y = range(10)
>>> print(y)
range(0, 10)
>>> squared_nums = [x**2 for x in range(10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num = [y**3 for y in range(5)]
>>> cube_num
[0, 1, 8, 27, 64]
```

`range()` defines the number range from start to finish, `range(0,10)` ranges from 0 to (10-1).

It's specially used in loop iterations, for example:
`squared_nums = [x**2 for x in range(10)]`

This is called **List Comprehension**, where we use the `for` loop to generate a result and also store it in a list simultaneously.

So, here we are using `range(10)`, which by default starts with 0 until (10-1). On each iteration, it assigns the number value 0, 1, 2, 3, ... to `x`, and then performs the operation `x**2`, which calculates `x` to the power of 2. After that, it stores each result in the list one by one. Finally, after finishing the loop, the list is assigned to the `squared_nums` variable.
