def get_http_error(error_code):
    """
    Returns the HTTP error message corresponding to the given error code.
    
    Args:
    error_code (int): The HTTP error code.
    
    Returns:
    str: The corresponding error message.
    """
    
    error_messages = {
        200: "OK",
        400: "Bad request",
        404: "Not found"
    }
    return error_messages.get(error_code, "Unknown error")

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
