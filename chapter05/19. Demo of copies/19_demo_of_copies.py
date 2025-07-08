import copy

def main():
    ages = [1, [2, 3, 4], 5]  # Original list with nested list

    # Method 1: Shallow copy using list slicing
    ages_slice = ages[:]
    # Method 2: Shallow copy using the list's copy method
    ages_cp = ages.copy()
    # Method 3: Shallow copy using the list constructor
    ages_list = list(ages)
    # Method 4: Deep copy using the 'copy' module
    ages_dcp = copy.deepcopy(ages)

    # Print the original list and its copies before modification
    print("Original list:", ages)
    print("Shallow copy (slicing):", ages_slice)
    print("Shallow copy (copy method):", ages_cp)
    print("Shallow copy (list constructor):", ages_list)
    print("Deep copy:", ages_dcp)

    # Modify the original list
    ages[0] = 100  # Change a non-nested element
    ages[1][0] = 200  # Change a nested element

    # Print the original list and its copies after modification
    print("\nAfter modifying the original list:")
    print("Original list:", ages)
    print("Shallow copy (slicing, nested list should change):", ages_slice)
    print("Shallow copy (copy method, nested list should change):", ages_cp)
    print("Shallow copy (list constructor, nested list should change):", ages_list)
    print("Deep copy (should not change):", ages_dcp)

if __name__ == "__main__":
    main()
