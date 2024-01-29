# How to Install Python and Set it to Local Environment

Before you can run the Python code, you need to make sure you have Python installed on your local machine. Here are the steps to install Python and set it to your local environment:

- Go to the official Python website at https://www.python.org/ and download the latest version of Python.
- Run the installer and make sure to check the box that says "Add Python to PATH" during installation.
- Open a terminal or command prompt and type `python --version` to check if Python is installed correctly.

## How to Call a Function in Python from Another Python File

In this project, we have two Python files: hello_chai.py and chai.py. The hello_chai.py file contains a chai function that prints a message to the console. The chai.py file calls the chai function from hello_chai.py.

To call a function from another Python file, you need to import the file containing the function. Here's how you can do it:

- Make sure both files are in the same directory.
- In chai.py, you can import the chai function like this:

```bash
from hello_chai import chai

chai("ginger tea")
```

## Running the Python Code in Terminal

To run the Python code in the terminal:

- Navigate to the directory containing the Python files using the cd command:

```bash
cd /path/to/directory/containing/python/files
```

- Run the chai.py file using the python command followed by the filename:

```bash
python chai.py
```

This will execute the chai.py file, which in turn calls the chai function from hello_chai.py.

- If you want to run the hello_chai.py file directly, use the following command:

```bash
python hello_chai.py
```
