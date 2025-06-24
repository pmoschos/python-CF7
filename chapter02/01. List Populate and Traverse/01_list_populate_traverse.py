ages = [19, 23, 34, 45]

print("Initial list of ages:", ages)

# Read: Iterating over a list and accessing both the index and the value
print("\nIterating with index and value:")
for index, value in enumerate(ages):  # (index, value)
    print(f"Index: {index}, Value: {value}")

# Iterating with enhanced for loop
print("\nIterating with enhanced for loop:")
for age in ages:
    print(age, end=" ")
print()

# Python's loop variables persist after the loop ends
print(f"\nVariable 'age' after the loop: {age}")