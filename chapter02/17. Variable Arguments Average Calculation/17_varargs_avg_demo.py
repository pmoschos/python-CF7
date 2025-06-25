def get_average(*numbers):
    """
    Calculate the average of a list of numbers and format the result to 2 decimal places.

    Parameters:
    *numbers: A variable number of numeric arguments.

    Returns:
    str: The formatted average of the input numbers.
    """
    if not numbers:
        return "No numbers provided."
    
    average = sum(numbers) / len(numbers)
    return "{:.2f}".format(average)

def main():
    # Example set of numbers
    numbers = [10, 20, 15]
    
    average = get_average(*numbers)
    print(f"The average of {numbers} is {average}")
    
    # Handling empty input
    average3 = get_average()
    print(f"Average with no input: {average3}")

if __name__ == "__main__":
    main()