# ASCII Art Generator 🎨

This project demonstrates how to convert a string into ASCII art using the `art` library in Python. Each character in the string is converted into its ASCII art representation, and the results are combined to form a cohesive piece of ASCII art text.

## Overview 🌟
The script converts a given string into ASCII art by:
1. Converting each character in the string to its ASCII art representation.
2. Ensuring all characters' ASCII art have the same height.
3. Combining the lines of ASCII art characters side by side.
4. Printing the combined ASCII art.

## 📸 Screenshots
![image](https://github.com/pmoschos/PythonScripts/assets/133533759/eea04c94-fa0a-405f-b3a0-1eded0767978)

## Script Description 📜

### `ascii_art_generator.py`
```python
# Import the required function from the art library
from art import text2art

# The word we want to convert to ASCII art
word = "Thank   you!"

# Convert each character in the word to its ASCII art representation
# and split each character's art into lines
ascii_art_lines = [text2art(char).split('\n') for char in word]

# Find the maximum height among all ASCII art characters
max_height = max(len(lines) for lines in ascii_art_lines)

# Ensure all characters' ASCII art have the same height
# by appending empty lines if necessary
for lines in ascii_art_lines:
    while len(lines) < max_height:
        lines.append(' ' * len(lines[0]))

# Combine the lines of ASCII art characters side by side
combined_art_lines = [''.join(line) for line in zip(*ascii_art_lines)]

# Print the combined ASCII art
print('\n'.join(combined_art_lines))
```

### Key Features 🌟
- **Character Conversion**: Converts each character in the string to its ASCII art representation.
- **Height Equalization**: Ensures all characters' ASCII art have the same height for proper alignment.
- **Side-by-Side Combination**: Combines the ASCII art representations of characters side by side.
- **Printing**: Prints the combined ASCII art to the console.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**:
  - `art`

### Usage Example 📋
1. **Install the `art` library if you haven't already**:
   ```bash
   pip install art
   ```
2. **Save the script as ascii_art_generator.py.**
3. **Run the script to generate and print the ASCII art:**
   ```bash
   python ascii_art_generator.py
   ```

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