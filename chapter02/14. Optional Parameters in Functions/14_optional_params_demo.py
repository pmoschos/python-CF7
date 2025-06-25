def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:
    """
    Returns a string representing a date in the format "dd/mm/yyyy".

    Args:
        day (int): The day of the month. Defaults to 1.
        month (int): The month of the year. Defaults to 1.
        year (int): The year. Defaults to 2000.

    Returns:
        str: The formatted date string.
    """
    return f"{day:02d}/{month:02d}/{year:4d}"

def main():
    """
    Demonstrates various ways to call get_formatted_date function.
    """
    print(get_formatted_date())  # Default date (01/01/2000)
    print(get_formatted_date(10))  # Date with day only (10/01/2000)
    print(get_formatted_date(14, 5))  # Date with day and month (14/05/2000)
    print(get_formatted_date(14, 5, 2024))  # Custom date (14/05/2024)
    print(get_formatted_date(year=2024))  # Custom date with keyword argument (01/01/2024)
    print(get_formatted_date(year=2024, day=14, month=5))  # Custom date with all arguments (14/05/2024)

if __name__ == "__main__":
    main()