# 🔄 Yield: Converts a Simple Function into a Generator 🌀

This script demonstrates how to use the `yield` statement to create a generator function in Python. It explains the concept of generator objects and how they preserve state between executions.

## Script Overview 📘

The script defines a simple generator function, `simple_generator`, which yields values one at a time, and demonstrates its usage by calling the `next()` function to retrieve values from the generator.

### :computer: Script Code

```python
# yield: converts a simple function into generator
# yield: returns a generator object

# When a generator function is called, it returns a generator object but does not start execution immediately.
# When the next() function is called on the generator object, the generator function starts executing until it
# reaches the yield statement. The value specified in the yield statement is returned to the caller, and the 
# state of the generator function is saved. The next time next() is called, the generator resumes execution 
# right after the yield statement, preserving the local variables and the execution state.
def simple_generator():
    print("First value")
    yield 1
    print("Second value")
    yield 2
    print("Third value")
    yield 3

def main():
    gen = simple_generator()

    print(next(gen))  # Output: First value \n 1
    print(next(gen))  # Output: Second value \n 2
    print(next(gen))  # Output: Third value \n 3

if __name__ == "__main__":
    main()
```

# Key Features 🌟
- **Yield Statement**: Learn how to use the yield statement to create generators.
- **Generator Objects**: Understand how generator objects work and how they preserve state between executions.
- **State Preservation**: See how the state of a generator function, including local variables and execution state, is saved between calls to next().

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `14_simple_generator.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `14_simple_generator.py`.
5. Run the script with: `python 14_simple_generator.py`.

## Usage Example 📋
Execute the script to see how the yield statement is used to create a generator. The script will demonstrate the behavior of the generator function, showing how it preserves state and yields values one at a time.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
