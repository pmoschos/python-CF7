def fibonacci():
    """
    Generator function to yield numbers in the Fibonacci sequence indefinitely.

    Yields:
    int: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    """
    Demonstrates the usage of the Fibonacci generator.
    """
    # Create a generator object for the Fibonacci sequence
    fib = fibonacci()

    # Print the first 10 numbers in the Fibonacci sequence
    print("First 10 numbers in the Fibonacci sequence:")
    for i in range(10):
        print(f"Fib({i}) = {next(fib)}")

    # Use the generator to find Fibonacci numbers below a certain threshold
    print("\nFibonacci numbers below 100:")
    fib = fibonacci()  # Reset the generator
    for num in fib:
        if num >= 100:
            break
        print(num)

    # Generate and collect Fibonacci numbers as a list
    print("\nCollect first 15 Fibonacci numbers as a list:")
    fib = fibonacci()  # Reset the generator
    fib_list = [next(fib) for _ in range(15)]
    print(fib_list)


if __name__ == "__main__":
    main()
