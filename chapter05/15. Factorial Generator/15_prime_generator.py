def is_prime(n):
    """
    Check if a number is a prime number.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_generator():
    """
    Generator function to yield prime numbers indefinitely.

    Yields:
    int: The next prime number in the sequence.
    """
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def main():
    """
    Demonstrates the usage of the prime number generator.
    """
    # Create a generator object for prime numbers
    primes = prime_generator()

    # Print the first 10 prime numbers
    print("First 10 prime numbers:")
    for _ in range(10):
        print(next(primes))

    # Print all prime numbers below 50
    print("\nPrime numbers below 50:")
    primes = prime_generator()  # Reset the generator
    for prime in primes:
        if prime >= 50:
            break
        print(prime)

    # Collect the first 15 prime numbers into a list
    print("\nCollect first 15 prime numbers as a list:")
    primes = prime_generator()  # Reset the generator
    prime_list = [next(primes) for _ in range(15)]
    print(prime_list)


if __name__ == "__main__":
    main()
