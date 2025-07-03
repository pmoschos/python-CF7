# 🔍 Function Arguments Demonstration Script 🔄

Welcome to the Function Arguments Demonstration Script! This script illustrates how to use positional, optional, additional positional (*args), and additional keyword arguments (**kwargs) in a Python function.

## Script Overview 📘

The script defines a function `test_args_func` that accepts various types of arguments and prints them out. The `main` function calls `test_args_func` with different combinations of arguments to demonstrate their usage.

### :computer: Script Code

```python
def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional positional (*args),
    and additional keyword arguments (**kwargs).
    
    Parameters:
    pos_arg1 (Any): The first positional argument.
    pos_arg2 (Any): The second positional argument.
    opt_arg1 (Any, optional): The first optional argument. Defaults to None.
    opt_arg2 (Any, optional): The second optional argument. Defaults to None.
    *args (tuple): Additional positional arguments.
    **kwargs (dict): Additional keyword arguments.
    """
    # Print positional arguments
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)
    
    # Print optional arguments
    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)
    
    # Print additional positional arguments if any
    if args:
        print("Additional positional arguments:")
        for arg in args:
            print(arg)
    
    # Print additional keyword arguments if any
    if kwargs:
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key} : {value}")

def main():
    # Call test_args_func with only positional and optional arguments
    test_args_func("Hello", "CF", opt_arg1=10, opt_arg2=100)
    print("-----------")
    
    # Call test_args_func with positional, optional, and additional keyword arguments
    test_args_func("Hello", "CF", opt_arg1=10, keyw_arg1="Python", keyw_arg2="Android")
    print("-----------")
    
    # Call test_args_func with positional, optional, additional positional, and additional keyword arguments
    test_args_func("Hello", "CF", # pos_arg1, pos_arg2
                   100, 200, # opt_arg1, opt_arg2
                   300, 400, # *args
                   kwargs1="Python", kwargs2="Android" # **kwargs
                   )

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Positional Arguments**: Learn how to use and print positional arguments in a function.
- **Optional Arguments**: Discover how to define and use optional arguments with default values.
- **Additional Positional Arguments**: Understand how to handle an arbitrary number of additional positional arguments using `*args`.
- **Additional Keyword Arguments**: See how to handle an arbitrary number of additional keyword arguments using `**kwargs`.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None (uses built-in Python functionalities)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `03_function_arguments.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `03_function_arguments.py`.
5. Run the script with: `python 03_function_arguments.py`.

## Usage Example 📋
Execute the script to see how different types of arguments are handled in a Python function. The script will print out each argument category for better understanding.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
