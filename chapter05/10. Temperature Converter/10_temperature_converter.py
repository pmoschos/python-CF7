def fahrenheit_to_celsius(temp: float) -> float:
    """
    Converts a Fahrenheit temperature to Celsius.
    
    Parameters:
    temp (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius rounded to two decimal places.
    """
    return round((temp - 32) * 5 / 9, 2)

def main():
    """
    Main function to demonstrate the conversion of Fahrenheit to Celsius using both
    list comprehension and generator expression.
    """
    fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]
    print("Fahrenheit temperatures:", fahrenheit_temps)

    # Convert temperatures using list comprehension
    celsius_temps_list = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps]
    print("\nCelsius temperatures (list comprehension):", celsius_temps_list)
    print("Type of celsius_temps_list:", type(celsius_temps_list))

    # Convert temperatures using generator expression
    celsius_temps_gen = (fahrenheit_to_celsius(temp) for temp in fahrenheit_temps)
    print("\nCelsius temperatures (generator expression):")
    print("Type of celsius_temps_gen:", type(celsius_temps_gen))

    # Iterating over the generator
    for celsius in celsius_temps_gen:
        print(celsius)

    # Attempting to reuse the generator
    print("\nRe-iterating over the generator:")
    for celsius in celsius_temps_gen:
        print(celsius)

if __name__ == "__main__":
    main()
