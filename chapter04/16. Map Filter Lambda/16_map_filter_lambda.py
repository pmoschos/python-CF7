# List of city names
cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

# Filtering city names longer than 5 characters using filter and lambda
long_cities = filter(lambda city: len(city) > 5, cities)

# Capitalizing the filtered city names using map and lambda
cap_length_cities = list(map(lambda city: city.title(), long_cities))

# All in one
# Filter and capitalize cities with more than 5 characters
cap_length_cities = list(map(lambda city: city.title(), filter(lambda city: len(city) > 5, cities)))

# Print the transformed list
print("Capitalized Cities with more than 5 characters:", cap_length_cities)

# For reference: Using list comprehension to achieve the same functionality
cap_length_cities_comprehension = [city.title() for city in cities if len(city) > 5]
print("Using list comprehension:", cap_length_cities_comprehension)
