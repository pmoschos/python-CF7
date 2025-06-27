def calculate_sum_and_product(upper_bound):
    """
    Calculates the sum and product of numbers from 1 to upper_bound.
    
    Args:
    upper_bound (int): The upper limit of the range.
    
    Returns:
    tuple: A tuple containing the sum and product.
    """
    total_sum = 0
    total_product = 1

    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i
    
    return total_sum, total_product

def main():
    try:
        upper_bound = int(input("Please insert a positive int: "))
        if upper_bound <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    
    total_sum, total_product = calculate_sum_and_product(upper_bound)
    
    print(f"Sum (1 - {upper_bound}): {total_sum:,}")
    print(f"Product (1 - {upper_bound}): {total_product:,}")

if __name__ == "__main__":
    main()
