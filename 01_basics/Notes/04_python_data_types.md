# Python Data Types and Objects

- **Number:** 12345, 4.564, 3+4j, 0b110, Decimal(), Fraction()
- **String:** 'spam', "Shivam's", b'a\x01c', u'sp\xc4m'
- **List:** [1, [2, 'three'], 4.5], list(range(10))
- **Tuple:** (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- **Dictionary:** {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
- **Set:** set('abc'), {'a', 'b', 'c'}
- **File:** open('eggs.txt'), open(r'C:\ham.bin', 'wb')
- **Boolean:** True, False
- **None:** None

- Functions, modules, classes
- **Advanced**: Decorators, Generators, Iterators, MetaProgramming

These are the data types and objects we work with in Python.

Now, let's explore some operations on these data types:

```python
>>> 12 + 15
27
# Addition operation

>>> 3.5 * 8
28.0
# Multiplication operation

>>> 2 ** 100
1267650600228229401496703205376
# Exponential operation: 2 to the power 100

>>> import math
# Importing the math library

>>> math.pi
3.141592653589793
# Accessing the value of pi from the math library

>>> import random
>>> random.random()
0.0327523642237747
# Generating a random number between 0 and 1

>>> random.choice([1,2,3,4,5,6,7,8,9,10])
8
# Randomly choosing an element from a list

>>> random.choice([1,2,3,4,5,6,7,8,9,10])
1

>>> random.choice([1,2,3,4,5,6,7,8,9,10])
6

>>> username = "shivam"
>>> len(username)
6
# Getting the length of the string

>>> username[0]
's'
# Accessing the first character of the string

>>> username[0] = "A"
# TypeError: 'str' object does not support item assignment
# Strings are immutable, so they cannot be modified

>>> username[-1]
'm'
>>> username[-2]
'a'
# Accessing characters using reverse indexing

>>> username[1:3]
'hi'
# String slicing: extracting characters from index 1 to 2

>>> dir(username)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# List of operations available for a string

>>> mylist = [123, "tea", 5.614]
>>> mylist
[123, 'tea', 5.614]
>>> len(mylist)
3
>>> mylist[0]
123
>>> mylist[-1]
5.614
# List operations

>>> myDict = {"one": 'lemon', "two": 'juice', "comic":'batman'}
>>> myDict
{'one': 'lemon', 'two': 'juice', 'comic': 'batman'}
# Dictionary definition

>>> myDict['comic']
'batman'
# Accessing values using keys

>>> myDict["three"]
# KeyError: 'three'
# Key not found in the dictionary

>>> myTup = (1,2,4,5)
# Tuple definition

>>> myTup[0]
1
>>> len(myTup)
4
# Tuple operations
```
