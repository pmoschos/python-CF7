def get_http_error(error_code):
    """
    Returns the HTTP error message corresponding to the given error code.
    
    Args:
    error_code (int): The HTTP error code.
    
    Returns:
    str: The corresponding error message.
    """
    result = ''
    match error_code:
        case 200:
            result = "OK"
        case 400:
            result = "Bad request"
        case 404:
            result = "Not found"
        case _:
            result = "Unknown error"
    return result

def main():
    error_code = 404
    print(get_http_error(error_code))

if __name__ == "__main__":
    main()
