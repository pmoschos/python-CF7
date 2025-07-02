from typing import List, Any

# Define a list containing elements of mixed types, including another list
my_list = [1, 2, "Hello", [3, 4, 5]]

def append_to_list(li: List[Any], element: Any) -> None:
    """
    Appends an element to the provided list.

    Parameters:
    li (List[Any]): The list to which the element will be appended.
    element (Any): The element to append to the list.
    """
    # Append the specified element to the list
    li.append(element)

# Call the function to append "CF" to 'my_list'
append_to_list(my_list, "CF")

# Iterate through each item in the list and print it
for item in my_list:
    print(item, end=", ")  # Output each element of the list
print()