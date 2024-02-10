## Dictionary in python

```python
>>> chai_types = {'Masala': "Spicy", "Ginger": "Zesty", "Green": "Mild"}
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Masala"]
'Spicy'
>>> chai_types.get("Ginger")
'Zesty'
>>> chai_types.get("Gingery")
>>> chai_types.get("Masala")
'Spicy'
>>> chai_types.get("Masalaa")
>>> chai_types["Masalaa"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Masalaa'
```

The dictionary data type takes values in curly braces `{}` and it takes items as key-value pairs. We can display values using its key like this: `chai_types["Masala"]` => "Spicy". Because a dictionary doesn't have an index like a list, it only has keys which we can define. We can also use `get()` like this: `chai_types.get("Ginger")` to get the value, 'Zesty' in this case. If `get()` couldn't find anything, it just shows nothing, but if we try to access using a key like this: `chai_types["Masalaa"]`, it will give us an error.

```python
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
>>> chai_types["Green"] = "Fresh"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
```

We can replace the value in a specific key like this: `chai_types["Green"] = "Fresh"`. Now the key "Green" has "Fresh" as its value.

```python
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for chai in chai_types:
...     print(chai)
...
Masala
Ginger
Green
>>> for chai in chai_types:
...     print(chai, chai_types[chai])
...
Masala Spicy
Ginger Zesty
Green Fresh
```

We can iterate through the dictionary using a for loop, and by default, it iterates through the keys and prints only the keys, not the values. However, we can also access the values using the keys like this: `print(chai, chai_types[chai])`, so on each iteration, it will print the key and then its value.

```python
>>> for key, values in chai_types.items():
...     print(key, values)
...
Masala Spicy
Ginger Zesty
Green Fresh
>>> if "Masala" in chai_types:
...     print("I have masala chai")
...
I have masala chai
>>> print(len(chai_types))
3
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
```

We can access items of a dictionary using `.items()` in a for loop. `items()` on each iteration returns the key-value pair. For that, we have to assign two variables in the for loop to catch the key-value pairs, and then we can perform any action on them. An `if` condition can check whether a key is present in the dictionary or not. `len()` gives the length of the dictionary. Here, it's giving 3 because Python considers the key-value pair as a single element in the dictionary.

```python
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> chai_types["Earl Gray"] = "Citrus"
>>> chai_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Gray': 'Citrus'}
>>> chai_types.pop("Ginger")
'Zesty'
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Gray': 'Citrus'}
>>> chai_types.popitem()
('Earl Gray', 'Citrus')
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
```

We can add new items like this: `chai_types["Earl Gray"] = "Citrus"`. It will add "Earl Gray" as the key and "Citrus" as the value. We can also use `pop()` to remove an item pair, but we need to mention the specific item key in `pop()` to remove it. `popitem()` on the other hand, by default, removes the last key-value pair.

```python
>>> chai_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del chai_types["Green"]
>>> chai_types
{'Masala': 'Spicy'}
>>> chai_types_copy = chai_types.copy()
```

`del` is also used to delete items, but it also removes the item from the memory reference. Speaking of reference, we can also create an exact copy of our dictionary using `copy()`. It doesn't just assign the same memory reference to the new variable, but it completely creates a new dictionary in memory and passes its reference to the new variable.

```python
>>> tea_shop = {
... "chai": {"Masala" : "Spicy", "Ginger": "Zesty"},
... "Tea": {"Green": "Mild", "Black": "Strong"}
... }
>>> tea_shop
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"]
'Zesty'
```

We can create a dictionary with key-value pairs, where the values themselves can be dictionaries with their own key-value pairs.

In the `tea_shop` dictionary, "chai" and "tea" are keys which have dictionaries as values. If we want to view the "chai" dictionary, we can write like this: `tea_shop["chai"]`, and its dictionary will be displayed as `{'Masala': 'Spicy', 'Ginger': 'Zesty'}`.

If we want to see a specific item of this dictionary, then we can write like this: `tea_shop["chai"]["Ginger"]`, which will give us `'Zesty'`. Here, we are trying to access the value of "Ginger" in the "chai" dictionary.

```python
>>> squared_num = {x: x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}
```

We can also use a for loop to define and write key-value pairs in a dictionary. So, on each iteration of a range starting from 0 to (6-1), the value of `x` will be the key, and its `x` to the power 2 will be its value.

`clear()` can clear all the key-value pairs in the dictionary.

```python
>>> keys = ["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
```

We can also create a dictionary using `dict.fromkeys(keys, default_value)`, where the first argument is the variable keys which will create keys, and the second argument is the default_value which will be used as values.

So here, a dictionary will be created which will have the keys as the items of the keys array, and each key will have the value "Delicious" because the default_value variable has a single item as a string.

Now, if we write `dict.fromkeys(keys, keys)`, it will create the keys using the items of the keys array, but their values will be the whole keys array.
