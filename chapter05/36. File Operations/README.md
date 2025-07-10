# 📂 File Operations Demo Script 📄

This Python script demonstrates file handling operations such as reading, creating, updating, and deleting files. It provides reusable functions to perform these operations and ensures proper error handling for robust execution.

---

## Script Overview 📘

The script defines the following file operation functions:

1. **`read_file`**: Reads and prints the content of a file along with its metadata.
2. **`read_file_contents`**: Reads and returns the content of a file as a string.
3. **`create_file`**: Creates a new file and writes initial content to it.
4. **`update_file`**: Appends new content to an existing file.
5. **`delete_file`**: Deletes a specified file.

It also includes a `main` function to demonstrate these operations sequentially.

### :computer: Script Code

```python
import os

def read_file(file_path):
    """
    Reads and prints the content of a file along with additional details.

    Parameters:
    file_path (str): The path to the file to be read.
    """
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist or is not a valid file.")
        return
    
    try:
        with open(file_path, 'r') as f:
            # Displaying file metadata
            print("Filename:", f.name)
            print("Closed:", f.closed)
            print("Opening mode:", f.mode)
            
            # Reading and printing file contents
            contents = f.read()
            print("Contents:", contents)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
    
    # Confirm that the file is closed
    print("File closed after with-block:", f.closed)

def read_file_contents(file_path):
    """
    Reads the content of a file and returns it.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    str: The content of the file.
    """
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist or is not a valid file.")
        return None

    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
    return None

def create_file(file_path, content):
    """
    Creates a new file with the given content.

    Parameters:
    file_path (str): The path to the file to be created.
    content (str): The content to write to the file.
    """
    try:
        with open(file_path, 'w') as f:
            f.write(content)
            print(f"File '{file_path}' created successfully with content.")
    except IOError as e:
        print(f"Error creating file '{file_path}': {e}")

def update_file(file_path, content):
    """
    Updates the content of an existing file by appending new content.

    Parameters:
    file_path (str): The path to the file to be updated.
    content (str): The content to append to the file.
    """
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist or is not a valid file.")
        return

    try:
        with open(file_path, 'a') as f:
            f.write(content)
            print(f"File '{file_path}' updated successfully with new content.")
    except IOError as e:
        print(f"Error updating file '{file_path}': {e}")

def delete_file(file_path):
    """
    Deletes the specified file.

    Parameters:
    file_path (str): The path to the file to be deleted.
    """
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist or is not a valid file.")
        return

    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except IOError as e:
        print(f"Error deleting file '{file_path}': {e}")

def main():
    """
    Main function to perform CRUD operations on files.
    """
    # Creating a new file
    print("Creating 'example.txt':")
    create_file('example.txt', "This is the initial content of the file.\n")
    print()

    # Reading and printing details and contents of the created file
    print("Reading 'example.txt':")
    read_file('example.txt')
    print()

    # Updating the file by appending new content
    print("Updating 'example.txt':")
    update_file('example.txt', "This is the appended content.\n")
    print()

    # Reading and printing updated contents of the file
    print("Reading updated 'example.txt':")
    read_file('example.txt')
    print()

    # Deleting the file
    print("Deleting 'example.txt':")
    delete_file('example.txt')
    print()

    # Attempting to read the deleted file
    print("Reading 'example.txt' after deletion:")
    read_file('example.txt')
    print()

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **File Metadata**: Displays file details such as name, mode, and status.
- **Error Handling**: Handles missing files and IO errors gracefully.
- **CRUD Operations**: Supports creating, reading, updating, and deleting files.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `36_file_operations.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `36_file_operations.py`.
5. Run the script with:

   ```bash
   python 36_file_operations.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Creating 'example.txt':
File 'example.txt' created successfully with content.

Reading 'example.txt':
Filename: example.txt
Closed: False
Opening mode: r
Contents: This is the initial content of the file.
File closed after with-block: True

Updating 'example.txt':
File 'example.txt' updated successfully with new content.

Reading updated 'example.txt':
Filename: example.txt
Closed: False
Opening mode: r
Contents: This is the initial content of the file.
This is the appended content.
File closed after with-block: True

Deleting 'example.txt':
File 'example.txt' deleted successfully.

Reading 'example.txt' after deletion:
Error: File 'example.txt' does not exist or is not a valid file.
```

---

## 📲 Contact and Contribution

### Contact 📧
- **Author**: Panagiotis Moschos
- **Email**: pan.moschos86@gmail.com
- **GitHub**: [pmoschos](https://github.com/pmoschos)

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>

