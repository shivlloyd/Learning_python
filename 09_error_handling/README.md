# Python project - Youtube manager app

```python
>>> x = ()
>>> x = ("Masala", "lemon", "ginger")
>>> y = enumerate(x)
>>> y
<enumerate object at 0x000001E6D849DD00>
>>> list(y)
[(0, 'Masala'), (1, 'lemon'), (2, 'ginger')]
```

in here tuple `x` is created with the values "Masala", "lemon", and "ginger". Then, it creates an enumerate object `y` from this tuple. An enumerate object is an iterator that generates index-value pairs, where the index represents the position of each value in the original tuple. Converting `y` to a list yields a list of tuples, where each tuple contains an index-value pair from the original tuple `x`. In this case, the resulting list is `[(0, 'Masala'), (1, 'lemon'), (2, 'ginger')]`, reflecting the positions and values of the elements in `x`.

`enumerate()` is a built-in Python function used to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of each item. It takes an iterable (like a list or tuple) as its argument and returns an enumerate object, which is an iterator that generates tuples. Each tuple contains two elements: the index of the item in the iterable and the item itself. This allows you to loop through the iterable and access both the index and the value of each item simultaneously, which can be useful in many programming scenarios, such as when you need to manipulate both the index and the value of elements within a loop.

```python
file = open("yotube.txt", "w")

try:
    file.write("chai aur code")
finally:
    file.close()

with open("yotube.txt", "w") as file:
    file.write("Chai aur python")
```

This code snippet demonstrates how to work with files in Python. Initially, it opens a file named "youtube.txt" in write mode using the `open()` function and assigns it to the variable `file`. Within a try block, it writes the string "chai aur code" to the file using the `write()` method. Regardless of whether an error occurs, the file is closed in the finally block to ensure proper resource cleanup and prevent file leakage.

Later, it employs a `with` statement, which is a context manager, to open the same file "youtube.txt" in write mode. This syntax ensures that the file is automatically closed after the nested block of code is executed, removing the need for an explicit call to `file.close()`. Within this block, it writes the string "Chai aur python" to the file using the `write()` method.

it shows two different methods to open and write to a file in Python, illustrating both the traditional `try-finally` approach and the more concise and recommended `with` statement for handling file operations.

```python
def load_data():
    pass


def list_all_videos(videos):
    pass


def add_video(videos):
    pass


def update_video(videos):
    pass


def delete_video(videos):
    pass


def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
```

This code defines a simple YouTube video manager application in Python. It consists of several functions for loading data, listing all videos, adding a new video, updating video details, and deleting a video. The `main()` function serves as the entry point of the program. Within `main()`, it loads initial data, presents a menu of options to the user using a while loop, and based on the user's choice, it calls corresponding functions to perform various actions on the video data.

Now, regarding `__name__`, it's a special built-in variable in Python. When a Python script is executed, Python sets the `__name__` variable to `"__main__"` if the script is being run directly. If the script is imported as a module into another script, `__name__` is set to the name of the module.

In this code, `if __name__ == "__main__":` checks whether the current script is being run directly. This is useful for distinguishing between whether the script is the main program or if it's being imported into another module. When the script is run directly, `main()` is called, initiating the execution of the program. If the script is imported elsewhere, `main()` won't be executed automatically. This allows the script to be reusable as a module in other programs without executing the main functionality when it's imported.

```python
>>> list = [{'name':'chai', 'time':'2min'}, {"name":"code", "time":"5min"}]
>>> list
[{'name': 'chai', 'time': '2min'}, {'name': 'code', 'time': '5min'}]
>>> for i in enumerate(list, start=1):'
...     print(i)
...
(1, {'name': 'chai', 'time': '2min'})
(2, {'name': 'code', 'time': '5min'})
>>> for i, video in enumerate(list, start=1):
...     print(f"{i}, {video['name']}")
...
1, chai
2, code
```

This code snippet demonstrates iterating over a list of dictionaries containing video details. Initially, it defines a list named `list` containing dictionaries, each representing a video with attributes like name and duration. The first loop utilizes `enumerate()` to generate index-value pairs for each dictionary in the list, starting the index from 1. It then prints each index-value pair, where the index represents the position of the video in the list, and the value is the corresponding dictionary containing video details.

In the second loop, it iterates over the list again using `enumerate()`, unpacking both the index and the dictionary representing a video. Within this loop, it prints the index alongside the name of the video extracted from the dictionary using `video['name']`. This results in a formatted display of the index followed by the name of each video in the list. The code showcases how to access and present specific information from a list of dictionaries using enumeration, facilitating easy retrieval and display of video details.

```python
import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
```

This code segment utilizes the `json` module in Python to load data from a file named "youtube.txt". Inside the `load_data()` function, it employs a `try-except` block to handle file operations. It attempts to open the file in read mode using the `open()` function within a `with` statement, which ensures proper file handling and automatic closing. If the file exists, it reads its contents using `json.load(file)` to deserialize the JSON data into a Python object and returns it. However, if the file is not found (`FileNotFoundError`), indicating that no data has been previously saved, it returns an empty list `[]`.

```python
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)
```

This code snippet defines a function named `save_data_helper()` responsible for saving data to a file named "youtube.txt". Within the function, it utilizes the `with` statement to open the file in write mode, ensuring proper file handling and automatic closure after the block of code executes. The `json.dump()` function is then employed to serialize the Python object `videos` into JSON format and write it to the file.

```python
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)
```

A function named `list_all_videos()` that takes a list of video as input. Within the function, it begins by printing a newline character and a line of asterisks to create a visual separator. Then, it utilizes a `for` loop with `enumerate()` to iterate over the list of videos, starting the index from 1. During each iteration, it prints the index, the name of the video extracted from the dictionary using `video['name']`, and the duration of the video extracted using `video['time']`. This creates a formatted display of all videos with their respective index, name, and duration. After iterating through all videos, it prints another line of asterisks to visually separate the list from other content.

```python
def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
```

function named `add_video()` is responsible for adding a new video to a list of video dictionaries. Within the function, it prompts the user to input the name and duration of the video using the `input()` function. It then creates a new dictionary representing the video with the provided name and time, and appends it to the existing list of videos. Additionally, it calls the `save_data_helper()` function to save the updated list of videos to a file, ensuring that the new video is persisted for future use.

```python
def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")
```

`update_video()` is responsible for updating the details of a specific video in the list of videos. Initially, it displays the current list of videos using the `list_all_videos()` function. Then, it prompts the user to input the index of the video they want to update. If the provided index is within the valid range of video indices (from 1 to the length of the videos list), it proceeds to prompt the user for the new name and time for the selected video. It then updates the video's details in the list using the provided information. Finally, it calls the `save_data_helper()` function to save the updated list of videos to a file. However, if the provided index is invalid, it notifies the user with a message stating "Invalid index selected".

```python
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")
```

`delete_video()` function is designed to remove a specific video from the list of videos. Initially, it displays the current list of videos using the `list_all_videos()` function. Then, it prompts the user to input the index of the video they wish to delete. If the provided index falls within the valid range of video indices (from 1 to the length of the videos list), it proceeds to delete the video from the list using the `del` statement. After removing the video, it calls the `save_data_helper()` function to update the list of videos stored in the file. However, if the provided index is invalid, indicating that the selected video does not exist in the list, it notifies the user with a message stating "Invalid video index selected".
