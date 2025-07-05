import time

def get_time(n):
    """
    Calculate the sum of the first n natural numbers and measure the time taken to perform the calculation.

    Parameters:
    n (int): The number of natural numbers to sum.

    Returns:
    int: The sum of the first n natural numbers.
    """
    # time.perf_counter() for high-resolution timing, especially useful for short computations.
    start_time = time.perf_counter() # .time()  # Record the start time
    # Perform the calculation: sum of the first n natural numbers
    result = sum(range(n))  # 0 + 1 + 2 + 3 + ... + (n - 1)
    end_time = time.perf_counter() # .time()  # Record the end time
    # Print the time taken to run the function
    print(f"My function took {end_time - start_time: .5f} seconds to run")
    
    return result

def main():
    """
    Main function to demonstrate the get_time function.
    """
    # Call the get_time function with n = 1,000,000 and print the result
    print(get_time(10000000))

if __name__ == "__main__":
    main()
