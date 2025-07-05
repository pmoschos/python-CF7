import time

def timer_decorator(func):
    """
    Decorator to measure the execution time of a function.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The decorated function with added timing functionality.
    """
    def inner_function(*args, **kwargs):
        """
        Wrapper function to calculate the execution time of the decorated function.

        Parameters:
        *args: Variable length argument list for the decorated function.
        **kwargs: Arbitrary keyword arguments for the decorated function.

        Returns:
        Any: The result of the decorated function.
        """
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the decorated function
        end_time = time.time()  # Record the end time
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to run.")
        return result  # Return the result of the decorated function
    return inner_function

# Decorate the sum_function manually
def sum_function(n):
    """
    Function to calculate the sum of integers from 0 to n-1.

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    int: The sum of integers from 0 to n-1.
    """
    return sum(range(n))

# Decorate the sum_function manually
sum_function = timer_decorator(sum_function)
print(sum_function(1_000_000))

# Decorate the sum_function_2 using the decorator syntax
@timer_decorator
def average_function(n):
    """
    Function to calculate the average of integers from 0 to n-1.

    Parameters:
    n (int): The upper limit of the range.

    Returns:
    float: The average of integers from 0 to n-1.
    """
    if n == 0:
        return 0
    total_sum = sum(range(n))
    return total_sum / n

print(average_function(1_000_000))

# Another example function decorated with the timer_decorator
@timer_decorator
def reverse_string(s):
    """
    Function to reverse a string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return "".join(reversed(s))

print(reverse_string("Coding Factory"))

def main():
    """
    Main function to demonstrate the usage of the timer_decorator.
    """
    print(sum_function(1_000_000))  # Manually decorated function
    print(average_function(1_000_000))  # Function decorated with @timer_decorator
    print(reverse_string("Coding Factory"))  # Another example function decorated with @timer_decorator

if __name__ == "__main__":
    main()
