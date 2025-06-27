def process_characters():
    """
    Reads characters from the user and prints their ASCII values until the user inputs '#'.
    """
    ch = input("Please insert a char: ")

    while ch != '#':
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
    
    print("Goodbye")

def process_characters2():
    """
    Reads characters from the user and prints their ASCII values until the user inputs '#'.
    """
    while True:
        ch = input("Please insert a char (or '#' to quit): ")
        if ch == '#':
            break
        print(f"{ch}: {ord(ch)}")
    
    print("Goodbye")

def main():
    process_characters()
    process_characters2()

if __name__ == "__main__":
    main()