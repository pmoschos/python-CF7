from collections import Counter

def count_with_dict_comprehension(my_list):
    """
    Count frequencies using dictionary comprehension.
    """
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print("\nDictionary Comprehension:", frequency_dict)

def count_with_manual_loop(my_list):
    """
    Count frequencies using a manual loop and conditional check.
    """
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    print("\nManual Loop:", frequency_dict)

def count_with_get_method(my_list):
    """
    Count frequencies using a manual loop with `get()` method for default values.
    """
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    print("\nManual Loop with get():", frequency_dict)

def count_with_counter(my_list):
    """
    Count frequencies using `Counter` from the `collections` module.
    """
    frequency_dict = Counter(my_list)
    print("\nUsing Counter:", frequency_dict)
    # Get elements sorted by frequency
    sorted_by_freq = frequency_dict.most_common()
    print("\nSorted by Frequency:", sorted_by_freq)

def main():
    # Original list of strings
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

    # Demonstrate different ways to count frequencies
    count_with_dict_comprehension(my_list)
    count_with_manual_loop(my_list)
    count_with_get_method(my_list)
    count_with_counter(my_list)

if __name__ == "__main__":
    main()
