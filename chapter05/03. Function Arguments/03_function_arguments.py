def test_args_func(pos_arg1, pos_arg2, opt_arg1=None, opt_arg2=None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional positional (*args),
    and additional keyword arguments (**kwargs).
    
    Parameters:
    pos_arg1 (Any): The first positional argument.
    pos_arg2 (Any): The second positional argument.
    opt_arg1 (Any, optional): The first optional argument. Defaults to None.
    opt_arg2 (Any, optional): The second optional argument. Defaults to None.
    *args (tuple): Additional positional arguments.
    **kwargs (dict): Additional keyword arguments.
    """
    # Print positional arguments
    print("Pos arg1:", pos_arg1)
    print("Pos arg2:", pos_arg2)
    
    # Print optional arguments
    print("Opt arg1:", opt_arg1)
    print("Opt arg2:", opt_arg2)
    
    # Print additional positional arguments if any
    if args:
        print("Additional positional arguments:")
        for arg in args:
            print(arg)
    
    # Print additional keyword arguments if any
    if kwargs:
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key} : {value}")

def main():
    # Call test_args_func with only positional and optional arguments
    test_args_func("Hello", "CF", opt_arg1=10, opt_arg2=100)
    print("-----------")
    
    # Call test_args_func with positional, optional, and additional keyword arguments
    test_args_func("Hello", "CF", opt_arg1=10, keyw_arg1="Python", keyw_arg2="Android")
    print("-----------")
    
    test_args_func("Hello", "CF", # pos_arg1, pos_arg2
                   100, 200, # opt_arg1, opt_arg2
                   300, 400, # *args
                   kwargs1="Python", kwargs2="Android" # **kwargs
                   )


if __name__ == "__main__":
    main()
