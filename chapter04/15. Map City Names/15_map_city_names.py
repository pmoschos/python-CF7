# List of city names
cities = ["london", "paris", "barcelona", "athens"]

# Using map and a lambda function to capitalize each city name
# The title() function is used to convert the first character of each word to uppercase and the rest to lowercase
cap_cities = list(map(lambda city: city.title(), cities))

# Printing the list of capitalized city names
print("Capitalized Cities:", cap_cities)
