```python
>>> x = 2
>>> y = 3
>>> z = 4
>>> x+y
5
>>> x + (y * z)
14
>>> 40 + 2.23
42.23
>>> "shivam" + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> int(2.23)
2
>>> float(40)
40.0
>>> "tea" + "tea"
'teatea'
```

Python treats numbers with precision. When performing expressions like x + y \* z, it is necessary to use parentheses to prioritize operations. Additionally, when performing operations between different data types, conversion into a similar data type is required. For example, "shivam" + 3 will result in an error because a string cannot be added to an integer. To convert a value into an integer data type, int() is used. Similarly, str() and float() are used for conversion into string and floating-point types, respectively. Adding two strings, as in "tea" + "tea," is called concatenation of strings and will yield the output "teatea."

```python
>>> x, y, z
(2, 3, 4)
>>> x+1, y*2
(3, 6)
>>> y%2
1
>>> z ** 2
16
>>> z**5
1024
>>> 100**2
10000
>>> 2**100
1267650600228229401496703205376
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

Whenever we write like this x, y, z, Python automatically combines their values into tuple format (2, 3, 4). To check the remainder of two values, we use the % operator (y%2 => 1) because the value of y is 3. Now, to calculate the power of two values, we use ** in Python (z ** 2 => 16). Python can also handle huge number values; even if we calculate 2\*\*1000, the value doesn't show using exponents but the actual long number, which other programming languages struggle to handle.

```python
>>> result = 1/3.0
>>> result
0.3333333333333333
>>> repr('chai')
"'chai'"
>>> str(123)
'123'
>>> print('chai')
chai
```

Dividing a number with a floating point results in floating-point numbers. `result = 1/3.0` => `0.3333333333333333`.
`repr()` is used to put everything into quotation marks. `repr('chai')` => `"'chai'"`.
`str()` converts anything into a string data type. `str(123)` => `'123'`.
`print()` prints the value into the console.

```python
>>> 1 < 2
True
>>> 5.0 == 5.0
True
>>> 4.0 != 5.0
True
>>> x, y, z
(2, 3, 4)
>>> x < y < z
True
>>> x < y and y < z
True
>>> x < y or y < z
True
>>> 1 == 2 < 3
False
>>> 1 == 2 and 2 < 3
False
```

The operators (<, >, <=, >=, ==, !=, and, or) produce only boolean output (True/False). The `and` operator gives True if both values are True. For example, in `(x < y and y < z)`, it will be True if both `x < y` AND `y < z` are True.

Similarly, in `(x < y or y < z)`, we need only one side to be True. For example, even if `x` is smaller than `y` and `y` is not smaller than `z`, `x < y or y < z` will result in True.

```python
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.floor(3.6)
3
>>> math.floor(3.9)
3
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8)
-2
```

In Python, the `math` library is very useful. `math.floor(3.5)` will give the closest value below the number, which in this case is 3. So, `math.floor(-3.5)` will give -4 because it's the closest value below the number.

`math.trunc(2.8)` gives the closest value toward 0 on the number line, so here it will result in 2. `math.trunc(-2.8)` gives -2 because it's the closest value towards 0.

```python
>>> 2 + 1j
(2+1j)
>>> (2 + 1j) * 3
(6+3j)
```

Python can handle imaginary numbers as well. `(2 + 1j) * 3` results in `(6+3j)`, where 3 is only multiplied by the real part, not the imaginary part.

```python
>>> 0o20
16
>>> 0xFF
255
>>> 0b11000
24
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
```

We can handle different number formats like octal, hexadecimal, and binary numbers in Python. Octal is denoted as `0o`, hexadecimal as `0x`, and binary as `0b`. Additionally, reverse operations can be performed to check octal, hexadecimal, and binary values for decimal values using `oct()`, `hex()`, and `bin()` respectively.

```python
>>> int('64', 8)
52
>>> int('64', 16)
100
>>> int('1100', 2)
12
```

We can also use `int()` to convert octal, hexadecimal, and binary numbers into decimal. For example, `int('1100', 2)` first takes the value we want to convert in string format, then after the comma, we provide the base value of the number format we are converting. Here, it's a binary number, so we enter 2, and the answer is 12. (The base for octal is 8, hexadecimal is 16, binary is 2, and decimal is 10.

```python
>>> import random
>>> random.random()
0.4265217694220802
>>> random.random()
0.2812037679620639
>>> random.randint(1, 100)
97
>>> random.randint(1, 100)
64
>>> random.randint(1, 100)
69
```

`random()` is used to generate random floating-point numbers between 0 and 1. `random.randint(1, 100)` is used to generate random integers between 1 and 100 (inclusive). Note that the upper limit (100 in this case) is included in the possible values.

```python
>>> li = ['lemon', 'masala', 'ginger', 'mint']
>>> random.choice(li)
'lemon'
>>> random.choice(li)
'mint'
>>> random.choice(li)
'masala'
>>> random.shuffle(li)
>>> li
['ginger', 'lemon', 'mint', 'masala']
>>> random.shuffle(li)
>>> li
['masala', 'mint', 'ginger', 'lemon']
```

The `random` library has various functions, such as `choice()`, which can be used to get random values from a list, and `shuffle()`, which can shuffle the order of items in that list.

```python
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3
5.551115123125783e-17
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
>>> from fractions import Fraction
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)
```

In Python, decimal handling can be challenging. For example, `0.1 + 0.1 + 0.1` should be equal to `0.3`, but Python shows `0.30000000000000004`. Similarly, `0.1 + 0.1 + 0.1 - 0.3` should be `0.0`, but Python shows `5.551115123125783e-17`. To address this issue, we can use `Decimal()` from the `decimal` library to work with decimals and get accurate results. Additionally, `Fraction()` from the `fractions` library can be used to handle fractional numbers. It's important to note that when using `Decimal('0.1')`, decimal values should be entered as strings. In `Fraction(2, 7)`, the first parameter is the numerator, and the second parameter is the denominator, representing the fraction 2/7.

```python
>>> setone = {1, 2, 3, 4}
>>> setone & {1, 3}
{1, 3}
>>> setone | {1, 3}
{1, 2, 3, 4}
>>> setone | {1, 3, 7}
{1, 2, 3, 4, 7}
>>> setone
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4}
set()
>>> type({})
<class 'dict'>
>>> type(setone)
<class 'set'>
```

A set is also treated as a collection in Python, and we can define a set like this: `setone = {1, 2, 3, 4}`. We can perform operations on sets, such as set intersections (`setone & {1, 3}` => `{1, 3}`) and set unions (`setone | {1, 3}` => `{1, 2, 3, 4}`). If we perform `setone - {1, 2, 3, 4}`, our set `setone` will be empty, but it won't show empty curly braces `{}`, because an empty `{}` denotes an empty dictionary, not an empty set. For an empty set, it's denoted as `set()`, so `setone - {1, 2, 3, 4}` => `set()`.

```python
>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True + 4
5
```

In Python, boolean values like `True` and `False` are treated as `1` and `0` behind the scenes. That's why `True == 1` is `True` and `False == 0` is `True`. The expression `True is 1` shows `False` because literally, `True` doesn't have a reference value of `1`. However, Python's internal processes treat `True` as `1` and `False` as `0`, explaining why `True + 4 = 5` in Python.
