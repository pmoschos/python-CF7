# yield: converts a simple function into generator
# yield: returns a generator object

# When a generator function is called, it returns a generator object but does not start execution immediately.
# When the next() function is called on the generator object, the generator function starts executing until it
# reaches the yield statement. The value specified in the yield statement is returned to the caller, and the 
# state of the generator function is saved. The next time next() is called, the generator resumes execution 
# right after the yield statement, preserving the local variables and the execution state.
def simple_generator():
    print("First value")
    yield 1
    print("Second value")
    yield 2
    print("Third value")
    yield 3

def main():
    gen = simple_generator()

    print(next(gen))  # Output: First value \n 1
    print(next(gen))  # Output: Second value \n 2
    print(next(gen))  # Output: Third value \n 3

if __name__ == "__main__":
    main()