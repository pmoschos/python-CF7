class FactoIterator:
    """
    An iterator class that generates factorials up to a given number n.
    """
    def __init__(self, n):
        """
        Initialize the iterator with the given number n.
        
        Parameters:
        n (int): The number up to which factorials are generated.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        self.n = n
        self.result = 1
        self.order = 1
    
    def __iter__(self):
        """
        Return the iterator object itself.
        
        Returns:
        self (FactoIterator): The iterator object itself.
        """
        return self
    
    def __next__(self):
        """
        Return the next factorial in the sequence.
        
        Returns:
        int: The next factorial in the sequence.
        
        Raises:
        StopIteration: When the sequence is complete.
        """
        if self.order > self.n:
            raise StopIteration
        
        self.result *= self.order
        self.order += 1
        return self.result

def main():
    """
    Main function to demonstrate the usage of the FactoIterator.
    """

    # Create a FactoIterator object to generate factorials up to 5
    facto_iter = FactoIterator(5)

    # Get the first factorial using the next() function
    a = next(facto_iter)
    print(a)  # Expected output: 1 (1!)

    # Iterate through the remaining factorials using a for loop
    for factorial in facto_iter:
        print(factorial)

    print("--------------------")
    new_facto_iter = FactoIterator(5)
    # Iterate through the remaining factorials using a for loop with enumerate
    for idx, factorial in enumerate(new_facto_iter, start=1):
        print(f"Factorial of {idx} is: {factorial}")

if __name__ == "__main__":
    main()
