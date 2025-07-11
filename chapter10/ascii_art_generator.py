# Import the required function from the art library
from chapter09.ascii_art_generator import text2art

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

