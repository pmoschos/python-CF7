def main():
    """
    Main function demonstrating in-place set operations.
    """
    # Define the original sets
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Elderberries"}
    store_b_products = {"Bananas", "Cherries", "Figs", "Grapes", "Honeydew"}

    print("Original Store A products:", store_a_products)
    print("Original Store B products:", store_b_products)

    # Intersection Update: Keep only products available in both stores
    store_a_products.intersection_update(store_b_products)
    print("Store A after intersection with Store B (common products):", store_a_products)

    # Reset store_a_products for next operation
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Elderberries"}

    # Union Update: Add all unique products from Store B to Store A
    store_a_products.update(store_b_products)
    print("Store A after union with Store B (all products):", store_a_products)

    # Reset store_a_products for next operation
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Elderberries"}

    # Difference Update: Remove products that are also in Store B
    store_a_products.difference_update(store_b_products)
    print("Store A after removing items found in Store B (exclusive to Store A):", store_a_products)

    # Reset store_a_products for next operation
    store_a_products = {"Apples", "Bananas", "Cherries", "Dates", "Elderberries"}

    # Symmetric Difference Update: Keep only products unique to each store
    store_a_products.symmetric_difference_update(store_b_products)
    print("Store A after symmetric difference with Store B (unique to each store):", store_a_products)

if __name__ == "__main__":
    main()
