# A program that simulates a message handler using the 'match' statement.

def handle_message(message):
    """
    Handles various types of messages using the 'match' statement.

    Args:
        message: The message to handle, which can be of various types such as string, list, dictionary, or tuple.
    """
    match message:
        # Case for a simple greeting message "hello"
        case "hello":
            print("Hello there! How can I help you today?")
        
        # Case for a goodbye message "bye"
        case "bye":
            print("Goodbye! Have a nice day!")
        
        # Case for a list containing "weather" and a location
        case ["weather", location]:
            print(f"Checking the weather for {location}...")
        
        # Case for a dictionary with a "greet" command and a name
        case {"command": "greet", "name": name}:
            print(f"Hello, {name}! Nice to meet you.")
        
        # Case for a dictionary with a "sum" command and exactly two numbers
        case {"command": "sum", "numbers": [a, b]}:
            print(f"The sum of {a} and {b} is {a + b}.")
        
        # Case for a dictionary with a "sum" command and a list of numbers
        case {"command": "sum", "numbers": numbers}:
            total = sum(numbers)
            print(f"The total sum is {total}.")
        
        # Case for a tuple where both values are identical
        case (x, y) if x == y:
            print(f"The values are identical: x = {x}, y = {y}")
        
        # Case for a tuple where values are different
        case (x, y):
            print(f"The values are different: x = {x}, y = {y}")
        
        # Default case for unrecognized message formats
        case _:
            print("Unrecognized message format.")


# Test various cases to help students understand how pattern matching works.
if __name__ == "__main__":
    # Simple literal matching
    handle_message("hello")  # Should print a greeting message
    handle_message("bye")    # Should print a goodbye message

    # List matching
    handle_message(["weather", "Athens"])  # Should print a weather check message for Athens

    # Dictionary matching
    handle_message({"command": "greet", "name": "Panagiotis"})  # Should greet Panagiotis
    handle_message({"command": "sum", "numbers": [5, 3]})        # Should print the sum of 5 and 3
    handle_message({"command": "sum", "numbers": [1, 2, 3, 4]})  # Should print the total sum of 1, 2, 3, and 4

    # Tuple matching and additional conditions
    handle_message((5, 5))  # Should indicate that the values are identical
    handle_message((7, 3))  # Should indicate that the values are different

    # Unrecognized pattern
    handle_message("unknown")  # Should indicate that the message format is unrecognized
