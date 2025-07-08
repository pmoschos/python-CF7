# 📊 Sales Analysis Script 💰

This Python script performs a comprehensive sales analysis for a business. It includes operations such as calculating monthly sales statistics, applying discounts, determining taxes, and identifying high-value months. The script provides detailed and well-organized outputs for each stage of the analysis.

---

## Script Overview 📘

The script processes monthly sales data and demonstrates the following functionalities:

1. **Data Validation**: Checks for missing or mismatched data.
2. **High Sales Filtering**: Filters months with sales greater than or equal to a specified threshold.
3. **Discount Application**: Applies discounts to sales above a defined value.
4. **Tax Calculation**: Calculates taxes for each month.
5. **Total and Average Sales**: Computes the total and average sales for the year.
6. **Best and Worst Months**: Identifies the best and worst performing months based on sales.

### :computer: Script Code

```python
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
```

---

## Key Features 🌟

- **Data Validation**: Ensures input data consistency and handles missing data gracefully.
- **Comprehensive Analysis**: Filters, calculates, and processes sales data with clear outputs.
- **Dynamic Discounts and Taxes**: Demonstrates real-world financial calculations for businesses.
- **Performance Insights**: Identifies key insights such as best and worst sales months.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses only built-in Python functionalities).

---

## Installation and Setup 🚀

No installation is required. Run the script directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `29_sales_analysis.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `29_sales_analysis.py`.
5. Run the script with:

   ```bash
   python 29_sales_analysis.py
   ```

---

## Usage Example 📋

### Expected Output

```plaintext
Monthly Sales (in thousands):
 {'January': 12000, 'February': 14500, ...}

Detailed Monthly Sales:
January  :  12000k
February :  14500k
...

High Sales Months (>= 15,000): {'April': 15000, 'May': 20000, ...}

Discounted Sales (10% discount for sales > 20,000): {'January': 12000, ...}

Monthly Taxes (15%): {'January': 1800.0, 'February': 2175.0, ...}

Total Annual Sales: 204,200k
Average Monthly Sales: 17,016.67k

Best Month: December with sales of 24,000k
Worst Month: January with sales of 12,000k
```

---

## 📲 Contact and Contribution

### Contact 📧
- **Author**: Panagiotis Moschos
- **Email**: pan.moschos86@gmail.com
- **GitHub**: [pmoschos](https://github.com/pmoschos)

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by 
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank