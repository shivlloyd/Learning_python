## Tuples in Python

The major difference between a list and a tuple is that lists are mutable, while tuples are immutable. This means that lists can be manipulated in memory locations, but tuples cannot.

```python
>>> tea_types = ("Black", "Green", "Oolong")
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0]
'Black'
>>> tea_types[-1]
'Oolong'
>>> tea_types[1:]
('Green', 'Oolong')
>>> tea_types[0] = "Lemon"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

We give items inside parentheses like this for tuple creation: `("Black", "Green", "Oolong")`, and we can also perform all the slicing and indexing operations similar to what we do with lists. However, if we try to change the value in a tuple, for example: `tea_types[0] = "Lemon"`, attempting to change the value at the 0th index, it will give an error.

```python
>>> len(tea_types)
3
>>> more_tea = ("Herbal", "Earl Grey")
>>> all_tea = more_tea + tea_types
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...     print("I have green tea")
...
I have green tea
>>> more_tea = ("Herbal", "Earl Gray", "Herbal")
>>> more_tea
('Herbal', 'Earl Gray', 'Herbal')
>>> more_tea.count("Herbal")
2
>>> more_tea.count("Herba")
0
```

`len()` tells the number of items in a tuple. We can also combine the values of two or more tuples into one and then assign the new tuple to any variable, like the `all_tea` variable being the combination of the `more_tea` tuple and `tea_types` tuple. We can also operate conditional statements on tuples like this: `if "Green" in all_tea:`.

`more_tea.count("Herbal")` counts the number of "Herbal" items present in the `more_tea` tuple. All these operations (`len()`, `count()`, `in`) can also be used with other data types like lists and strings, not just with tuples.

```python
>>> tea_types
('Black', 'Green', 'Oolong')
>>> (black, green, Oolong) = tea_types
>>> black
'Black'
>>> (tea1, tea2, tea3) = tea_types
>>> tea1
'Black'
>>> tea2
'Green'
>>> tea3
'Oolong'
>>> type(tea_types)
<class 'tuple'>
```

This is called tuple unpacking in Python. It allows you to assign values from a tuple to multiple variables in a single line of code. When you write `(tea1, tea2, tea3) = tea_types`, Python assigns the values from the `tea_types` tuple to `tea1`, `tea2`, and `tea3` respectively, based on their position in the tuple. This is a convenient way to quickly assign multiple variables at once. We can also check the datatype using the `type()` method.
