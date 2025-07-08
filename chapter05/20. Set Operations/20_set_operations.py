def main():
    """
    Demonstrates set operations.
    """
    # Define two sets of products available in two different stores
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Watermelons"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Melons"}

    # Find common products (intersection) available in both stores
    common_products = store_a_products & store_b_products
    print("Products available in both Store A and Store B:", common_products)
    # Alternatively, using the intersection method
    common_products = store_a_products.intersection(store_b_products)
    print("Products available in both Store A and Store B:", common_products)

    # Find all unique products (union) across both stores
    all_products = store_a_products | store_b_products
    print("All unique products across Store A and Store B:", all_products)
    # Alternatively, using the union method
    all_products = store_a_products.union(store_b_products)
    print("All unique products across Store A and Store B:", all_products)

    # Find products available in Store A but not in Store B (difference)
    store_a_exclusive = store_a_products - store_b_products
    print("Products available only in Store A:", store_a_exclusive)
    # Alternatively, using the difference method
    store_a_exclusive = store_a_products.difference(store_b_products)
    print("Products available only in Store A:", store_a_exclusive)

    # Find products available in Store B but not in Store A (difference)
    store_b_exclusive = store_b_products - store_a_products
    print("Products available only in Store B:", store_b_exclusive)
    # Alternatively, using the difference method
    store_b_exclusive = store_b_products.difference(store_a_products)
    print("Products available only in Store B:", store_b_exclusive)

    # Find products that are in either Store A or Store B but not in both (symmetric difference)
    unique_to_either_store = store_a_products ^ store_b_products
    print("Products available in either Store A or Store B but not both:", unique_to_either_store)
    # Alternatively, using the symmetric_difference method
    unique_to_either_store = store_a_products.symmetric_difference(store_b_products)
    print("Products available in either Store A or Store B but not both:", unique_to_either_store)

if __name__ == "__main__":
    main()
