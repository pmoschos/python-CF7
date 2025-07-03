from datetime import datetime

def log_event(event_type: str, **kwargs: dict) -> None:
    """
    Logs an event with a specified type and additional keyword arguments.

    Parameters:
    event_type (str): The type of event being logged.
    kwargs (dict): Additional information about the event.
    """
    timestamp = datetime.now().isoformat()
    print(f"Event type: {event_type}")
    print(f"Timestamp: {timestamp}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("-" * 40)  # Separator for readability

def main() -> None:
    """
    Main function for testing the log_event function.
    """
    # Example usage of the log_event function
    log_event("UserLogin", user="JohnDoe", status="Success", ip="192.168.1.1")
    log_event("FileUpload", user="JaneDoe", status="Failure", filename="report.pdf", reason="File too large")

if __name__ == "__main__":
    main()
