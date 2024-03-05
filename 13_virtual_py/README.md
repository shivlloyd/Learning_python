# Python Virtual Environment Cheatsheet

**Create a new virtual environment**

- Use `python -m venv env_name` to create a new virtual environment named `env_name`.

**Install packages**

- Install packages using `pip install package_name`.

**Save installed packages to a file**

- Save installed packages to a file with `pip freeze > requirements.txt` or `pip list --format=freeze > requirements.txt`.

**Install packages from a file**

- Install packages from a file using `pip install -r requirements.txt`.

**Deactivate the current virtual environment**

- Use `deactivate` to deactivate the current virtual environment.

**Activate the new Python environment (Linux/Mac)**

- Activate the new Python environment in Linux or Mac with `source env_name/bin/activate`.

**Activate the new Python environment (Windows)**

- Activate the new Python environment in Windows with `.\env_name\Scripts\activate`.

**Explanation:**
Python virtual environments are like isolated containers where you can install packages separately from the system-wide Python installation. This allows you to work on different projects with their own dependencies without worrying about conflicts. Here's a breakdown of the commands:

- **Creating a new virtual environment** (`python -m venv env_name`): This command sets up a new environment with its own isolated Python installation.

- **Installing packages** (`pip install package_name`): Once inside the virtual environment, you can install packages specific to your project using pip.

- **Saving installed packages to a file** (`pip freeze > requirements.txt`): This command saves a list of all installed packages and their versions to a file called `requirements.txt`, which can be shared with others or used to recreate the environment.

- **Installing packages from a file** (`pip install -r requirements.txt`): This command installs all the packages listed in `requirements.txt`, ensuring that the environment has exactly the same dependencies as when the file was created.

- **Deactivating the current virtual environment** (`deactivate`): This command exits the virtual environment and returns you to the system-wide Python installation.

- **Activating the new Python environment (Linux/Mac)** (`source env_name/bin/activate`): This command activates the virtual environment, allowing you to work within its isolated environment.

- **Activating the new Python environment (Windows)** (`.\env_name\Scripts\activate`): This command activates the virtual environment on Windows, similarly allowing you to work within its isolated environment.
