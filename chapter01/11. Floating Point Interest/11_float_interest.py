# Amount of the principal loan/deposit
amount = 215_000.0  # underscore for readability (Python 3.6+ feature)

# Annual interest rate (as a decimal)
rate = 0.25

# Calculate interest
interest = amount * rate

# Print the total interest, formatted to two decimal places
print(f"Total interest: ${interest:,.2f}")
