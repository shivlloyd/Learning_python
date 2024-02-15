## Behind the scene of loops in python

![Screenshot 2024-02-15 123725](https://github.com/shivlloyd/Learning_python/assets/41133545/ed7f3466-0960-47f3-b0e9-21cbb3a38d9e)

Python uses its iteration tools for its behind-the-scenes loop operations. Iteration tools, such as "for" loops and comprehensions, are only applicable to objects that are iterable. Examples of iterable objects include lists, files, etc.

When iteration tools query iterable objects for applying loops on them, they pass an `iter()` method. These iterable objects return the memory address location of the starting point of the iterable object along with a `__next__` response, dictating to the iteration tool that there is more sequence of memory references for continuous iteration on each item.

After the iteration tool reaches the final `__next__` response, a StopIteration exception is raised, indicating to the iteration tool that the last item of the iterable object has been reached, and it is time to terminate the loop.

```python
>>> f = open('script.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'\n'
>>> f.readline()
'print("Chai is coming")\n'
>>> f.readline()
'username = "shivam"\n'
>>> f.readline()
'print(username)\n'
>>> f.readline()
''
>>> f.readline()
''
```

First, we create a file named `script.py`. Then, using `open()`, we can access that file and assign it to a variable called `f`. Now, `f.readline()` will read and print the first line of the file `script.py`, and continuous use of `f.readline()` will keep printing one line after another. After it has finished reading all the lines, it will start printing an empty string.

```python
>>> f = open('script.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'\n'
>>> f.__next__()
'print("Chai is coming")\n'
>>> f.__next__()
'username = "shivam"\n'
>>> f.__next__()
'print(username)\n'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Now, we have reloaded the `script.py` file into the variable `f` using `f = open('script.py')`. If we write `f.__next__()`, it will do the same thing as `readline()`, but it's a raw way of doing things. It will start iterating and printing the lines, but after the final line is printed, it will invoke the StopIteration exception, stopping the iteration.

```python
>>> for line in open('script.py'):
...     print(line)
...
import time



print("Chai is coming")

username = "shivam"

print(username)

>>> for line in open('script.py'):
...     print(line, end='')
...
import time

print("Chai is coming")
username = "shivam"
print(username)
```

`for` loop is another iter tool we can use to iterate on file, here we are using it to print the lines of the file.

```python
>>> f = open('script.py')
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
...
import time

print("Chai is coming")
username = "shivam"
print(username)
```

We can also use a while loop to iterate through the file's lines. We just have to specify to break out of the while loop if the iteration finishes using `if not line: break`. The `not` keyword negates the boolean value, checking if the variable `line` evaluates to False, meaning it's either an empty string or equivalent to None. If `line` is empty, `not line` evaluates to True, causing the loop to exit using the `break` statement.

```python
>>> myList = [1, 2, 3, 4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x00000250C848D9C0>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x00000250C848D9C0>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

`iter()` takes an iterable object like a list and can iterate through its items. So, when `iter(myList)` is executed, it passes its reference to a variable `I`, and now `I` contains the first starting memory reference of the list. Now, we start the iteration using `I.__next__()` and continue the iteration. The main thing to note is that `I` will still hold the memory reference of the first item; it only changes behind the scenes while iterating but still points to the same starting position. After the iteration reaches the last item, it will invoke the StopIteration to stop the looping.

```python
>>> f = open('script.py')
>>> iter(f) is f
True
>>> iter(f) is f.__iter__()
True
>>> my_new_list = [1,2,3]
>>> iter(my_new_list) is my_new_list
False
```

While iterating through a file, we don't have to use `iter()` explicitly because Python uses it by default behind the scenes. All we have to do is first open the file and pass its reference to a variable like this: `f = open('script.py')`. `iter(f) is f` returns True because `f` now contains the same memory reference as `iter(f)`.

However, while iterating through a list, we first have to make it iterable using `iter(my_new_list)`. That's why `iter(my_new_list) is my_new_list` returns False because `my_new_list` contains only the list memory reference, but `iter(my_new_list)` contains the iterable memory reference of the first item of that list, making it iterable.

When we store a file in a variable like this: `f = open('script.py')`, it becomes by default iterable without using `iter()`.

```python
>>> D = {'a': 1, 'b':2}
>>> for key in D.keys():
...     print(key)
...
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x00000250C81DDD00>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

We can also iterate through a dictionary. Using `for key in D.keys():`, we can automatically iterate through the keys in the dictionary.

However, for manual iteration, we can use `I = iter(D)`, which will pass the memory reference to the variable `I`. Now, we can use `next(I)` to iterate through one item after another, and after it reaches the end, it will raise the StopIteration exception.

```python
>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

now we can also use this manual iteration using `iter()` to iterate through `range()`.
