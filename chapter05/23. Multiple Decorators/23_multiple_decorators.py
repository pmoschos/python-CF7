import time

def log_calls(func):
    """
    A decorator that logs the function call.
    """
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    """
    A decorator that measures the execution time of the function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time of '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# The decorators are applied bottom-to-top (@measure_time first, then @log_calls).
# The execution is top-to-bottom (@log_calls executes first, then @measure_time).
@log_calls
@measure_time
def say_hello(name):
    """
    A simple function that returns a greeting.
    
    Args:
    name (str): The name to greet.
    
    Returns:
    str: The greeting message.
    """
    time.sleep(1)  # Simulate some processing delay
    return f"Hello, {name}!"

def main():
    # Using the function with multiple decorators
    print(say_hello("Alice"))
    print(say_hello("Bob"))

if __name__ == '__main__':
    main()
