import point as p

def main():
    """
    Main function to demonstrate Point operations.
    """
    p1 = p.Point(1, 2)
    p2 = p.Point(3, 4)
    p3 = p.Point(4, 5)

    print("Points:")
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    print(f"p3: {p3}")

    try:
        p4 = p1 + p2
        print("\nAddition of points (p1 + p2):")
        print(f"p4: {p4}")
    except TypeError as e:
        print(f"Error: {e}")

    print("\nEquality checks:")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p2 == p3: {p2 == p3}")
    print(f"p1 == p3: {p1 == p3}")

if __name__ == "__main__":
    main()

