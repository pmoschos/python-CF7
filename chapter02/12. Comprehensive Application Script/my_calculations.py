num1 = 100

def my_add_function(n, m):
    return n + m

def main():
    print("Value of num1:", num1)
    result = my_add_function(50, 75)
    print("result:", result)
    print(__name__) # ? __main__ ?

main()

#if __name__ == "__main__":
#    main()