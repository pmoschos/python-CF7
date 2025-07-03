from datetime import datetime, timedelta

def european_datetime_example():
    """
    Demonstrates datetime handling in a European format (DD/MM/YYYY and 24-hour clock).
    """

    print("\n1. Current Date and Time")
    # 1. Current Date and Time
    now = datetime.now()
    print(f"Current Date and Time: {now}")
    print(f"European Format: {now.strftime('%d/%m/%Y %H:%M:%S')}")

    print("\n2. Creating a Specific Date and Time")
    # 2. Creating a Specific Date and Time
    specific_date = datetime(2024, 12, 25, 15, 30)  # Christmas Day 2024, 15:30
    print(f"\nSpecific Date and Time: {specific_date.strftime('%d/%m/%Y %H:%M')}")

    print("\n3. Parsing a European Date String")
    # 3. Parsing a European Date String
    european_date_str = "03/12/2024 14:45"  # DD/MM/YYYY HH:MM
    parsed_date = datetime.strptime(european_date_str, '%d/%m/%Y %H:%M')
    print(f"\nParsed Date and Time from String: {parsed_date.strftime('%d/%m/%Y %H:%M')}")

    print("\n4. Date Arithmetic")
    # 4. Date Arithmetic
    one_week_later = parsed_date + timedelta(weeks=1)
    print(f"\nOne Week Later: {one_week_later.strftime('%d/%m/%Y %H:%M')}")
    
    five_days_before = parsed_date - timedelta(days=5)
    print(f"Five Days Before: {five_days_before.strftime('%d/%m/%Y %H:%M')}")

    print("\n5. Comparing Dates")
    # 5. Comparing Dates
    today = datetime.now()
    print("\nComparing Dates:")
    if parsed_date > today:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is in the future.")
    elif parsed_date < today:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is in the past.")
    else:
        print(f"{parsed_date.strftime('%d/%m/%Y %H:%M')} is today.")

    
    print("\n6. Formatting Options in European Style")
    # 6. Formatting Options in European Style
    print("\nVarious European Date Formats:")
    print(f"Day-Month-Year: {now.strftime('%d-%m-%Y')}")
    print(f"Full Date (Textual): {now.strftime('%A, %d %B %Y')}")
    print(f"Time (24-Hour Clock): {now.strftime('%H:%M:%S')}")

    print("\n7. Localized DateTime (Requires Babel for Full Localization)")
    # 7. Localized DateTime (Requires Babel for Full Localization)
    # pip install babel
    try:
        from babel.dates import format_datetime
        print("\nLocalized DateTime Example:")
        print(format_datetime(now, format='full', locale='fr_FR'))  # French
        print(format_datetime(now, format='full', locale='de_DE'))  # German
    except ImportError:
        print("\nInstall Babel to support full localized formatting.")

if __name__ == "__main__":
    european_datetime_example()
