# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers (iterator)
even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)

print(even_numbers_iterator)
# print(*even_numbers_iterator)
# print(*even_numbers_iterator)

# Printing ven numbers
for num in even_numbers_iterator:
    print(num, end=" ")

# Printing ven numbers ???
for num in even_numbers_iterator:
    print(num, end=" ")

# Using filter and lambda to create a list of even numbers from the original list
even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))

# Since even_numbers_list is already a list, you can directly reuse it
print("Repeated print of the even numbers list:")
print(even_numbers_list)
print(even_numbers_list)
