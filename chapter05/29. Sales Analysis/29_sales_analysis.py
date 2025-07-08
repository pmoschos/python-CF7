from functools import reduce

def main():
    """
    Main function to demonstrate a realistic sales analysis for a business.
    This includes monthly sales, discounts, taxes, filtering high-value months,
    and total revenue calculation.
    """
    # Define monthly sales data for a year (in thousands of currency units)
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    sales = [12_000, 14_500, 13_200, 15_000, 20_000, 18_500, 16_000, 15_500, 14_000, 19_000, 22_500, 24_000]

    # Handle edge case: empty or mismatched data
    if not months or not sales:
        print("No sales data available.")
        return
    if len(months) != len(sales):
        print("Error: Months and sales data length mismatch.")
        return

    # Create sales dictionary
    monthly_sales = dict(zip(months, sales))
    print("Monthly Sales (in thousands):\n", monthly_sales)

    print("\n-------------------")
    print("Detailed Monthly Sales:")
    for month, value in monthly_sales.items():
        print(f"{month:<9}: {value:>6}k")

    print("\n-------------------")
    # Filter months with sales >= 15,000
    high_sales_months = {month: value for month, value in monthly_sales.items() if value >= 15_000}
    if high_sales_months:
        print("High Sales Months (>= 15,000):", high_sales_months)
    else:
        print("No months with sales >= 15,000.")

    print("\n-------------------")
    # Apply a 10% discount for all sales above 20,000
    discounted_sales = {
        month: value * 0.9 if value > 20_000 else value
        for month, value in monthly_sales.items()
    }
    print("Discounted Sales (10% discount for sales > 20,000):\n", discounted_sales)

    print("\n-------------------")
    # Calculate taxes for each month at a rate of 15%
    monthly_taxes = {month: value * 0.15 for month, value in monthly_sales.items()}
    print("Monthly Taxes (15%):\n", monthly_taxes)

    print("\n-------------------")
    # Calculate total and average sales
    total_annual_sales = sum(monthly_sales.values())
    print("Total Annual Sales:", f"{total_annual_sales:,}k")

    average_monthly_sales = total_annual_sales / len(monthly_sales)
    print("Average Monthly Sales:", f"{average_monthly_sales:.2f}k")

    # Identify the best and worst performing months
    best_month = max(monthly_sales, key=monthly_sales.get)
    worst_month = min(monthly_sales, key=monthly_sales.get)
    print("\nBest Month:", best_month, f"with sales of {monthly_sales[best_month]:,}k")
    print("Worst Month:", worst_month, f"with sales of {monthly_sales[worst_month]:,}k")

if __name__ == "__main__":
    main()
