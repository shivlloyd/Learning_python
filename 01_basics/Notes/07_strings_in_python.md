## Strings in Python

Today we are going to learn about strings in Python.

```python
chai = "Lemon Tea"
chai
'Lemon Tea'
chai = "Masala Chai"
chai
'Masala Chai'
first_char = chai[0]
print(first_char)
M
chai
'Masala Chai'
slice_chai = chai[0:6]
print(slice_chai)
Masala
chai[0:6]
'Masala'
```

Here we can access characters of any string using its index. For example, `first_char = chai[0]` and `print(first_char)` => M. We can also perform string slicing. For example, `slice_chai = chai[0:6]` and `print(slice_chai)` => Masala. Here `chai[0:6]` explains that it only takes indices from 0 to 5 because the last number is one less than itself, so it includes characters only from index 0 to index 5 which is 'Masala'.

```python
num_list = '0123456789'
num_list[:]
'0123456789'
num_list[3:]
'3456789'
num_list[:7]
'0123456'
num_list[0:7:2]
'0246'
num_list[0:7:3]
'036'
```

Now we can do more operations on strings using slicing. For example, `num_list[3:]  => '3456789'` starts from 3 and goes till the end of the string. `num_list[:7] => '0123456'` starts from 0 and goes till (7-1). `num_list[0:7:2] => '0246'` here it goes normally from 0 to (7-1) but it skips one number every time. `num_list[0:7:3] => '036'` similarly here it skips 2 numbers every time.

```python
chai
'Masala Chai'
print(chai.lower())
masala chai
print(chai.upper())
MASALA CHAI
chai
'Masala Chai'
chai = "  Masala Chai  "
chai
'  Masala Chai  '
print(chai.strip())
Masala Chai
chai = "Lemon Chai"
print(chai.replace("Lemon", "Ginger"))
Ginger Chai
chai
'Lemon Chai'
```

Now we can apply some methods on our string. `.lower()` converts our string into lower case. `.upper()` converts our string into upper case. `.strip()` removes extra space from the front and back of our string. `.replace()` first takes the string which needs to be replaced and after that the string which will replace it. For example, `chai = "Lemon Chai"` and `print(chai.replace("Lemon", "Ginger"))` => Ginger Chai. "Lemon" is replaced with "Ginger" but even after all these operations, the original string won't change simply because strings are immutable.

```python
chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
chai = "Masala Chai"
print(chai.find("Chai"))
7
print(chai.find("Coffee"))
-1
chai = "Masala chai chai chai"
print(chai.count("chai"))
3
```

Now we can convert strings into a list using the `split()` method. For example, `chai = "Lemon, Ginger, Masala, Mint"` and `print(chai.split(", "))` => ['Lemon', 'Ginger', 'Masala', 'Mint']. Here `split` takes ", " which means split this string on the basis of "," and spacing " ". Wherever it encounters ", " it will create a split and consider it an element for the list. By default, `split()` splits on the basis of spaces, but we can mention the positions to split manually like ", ".

`.find()` finds the requested string and gives the index from which that string starts. If it's unable to find that string, it gives -1. `.count()` counts the number of times that string occurs.

```python
chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
order
'I ordered {} cups of {} chai'
print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai
order
'I ordered {} cups of {} chai'
```

Here these `{}` curly braces are known as placeholders, and `order.format(quantity, chai_type)` instructs to place the value of these two variables in those `{}` curly braces respectively, resulting in => "I ordered 2 cups of Masala chai".

```python
chai_variety = ['Lemon', 'Ginger', 'Masala', 'Mint']
chai_variety
['Lemon', 'Ginger', 'Masala', 'Mint']
print("".join(chai_variety))
LemonGingerMasalaMint
print(" ".join(chai_variety))
Lemon Ginger Masala Mint
print("-".join(chai_variety))
Lemon-Ginger-Masala-Mint
print(", ".join(chai_variety))
Lemon, Ginger, Masala, Mint
```

Now let's convert that list back to a string. For that, we use `"".join()` method and in those "" we can enter values using which we can join those list items. For example, `print("-".join(chai_variety))` => Lemon-Ginger-Masala-Mint, it puts "-" between the items and then converts it into strings.

```python
chai = "Masala Chai"
len(chai)
11
chai
'Masala Chai'
for letter in chai:
    print(letter)
M
a
s
a
l
a

C
h
a
i
```

`len()` gives us the number of characters of that string. We can print each character of a string using a for loop. `for letter in chai:` iterates through each character of that string and then assigns each character to the variable letter and then performs the operations mentioned after the indentation. Here we are telling it to print the letter.

```python
chai = "He said, \"Masala chai is awesome\" "
chai
'He said, "Masala chai is awesome" '
chai = "Masala\nChai"
chai
'Masala\nChai'
print(chai)
Masala
Chai
chai = r"Masala\nChai"
print(chai)
Masala\nChai
```

We use a backslash before `"\"` to maintain the "" in our string. `\n` means we want to print string after `\n` in the new line. But if we don't want to print it new line and still we need `\n` in our string then we use a raw string like this `chai = r"Masala\nChai"`. `print(chai)` => Masala\nChai.

```python
chair = r"c:\user\programFiles"
chai = r"c:\user\

programFiles"
print(chai)
c:\user\programFiles
chai = "c:\\user\\programFiles"
print(chai)
c:\user\programFiles
```

We use raw string mainly to include special characters like `\` in a string. If we don't want to use a raw string but still include `\`, then we must write like this `"\\",` it will be treated as single `"\"`. Otherwise, if we use directly `"\"`, without using a raw string then it will give a SyntaxError.

```python
chai = "Masala chai"
print("Masala" in chai)
True
print("Ginger" in chai)
False
```

We can also check whether a sequence of characters is present in a string or not. `print("Masala" in chai)` here it's checking that "Masala" is present in the string chai or not and it will only result in boolean values (True/False).
