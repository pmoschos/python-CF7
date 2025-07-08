import logging

def main():
    log_file = 'cf6.log'

    # Create a file handler for logging to a file
    # So, we use this approach to redirect the error from our console to the logging file.
    file_handler = logging.FileHandler(log_file, mode='a')

    # Create a list of handlers for the logger
    handlers = [file_handler]

    # Name of the Logger
    logger = logging.getLogger('search-app')

    # Configure the root logger with the handlers list
    logging.basicConfig(
        handlers=handlers, 
        level=logging.INFO, # Logging Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    )

    # List of numbers to search within
    nums = [10, 20, 30, 40, 50]
    # Number to find in the list
    num_to_find = 20

    try:
        # Attempt to find the index of num_to_find in nums
        index = nums.index(30)
        print('Found!')
        print(index)
    except ValueError as e:
        # Log an error if num_to_find is not found in nums
        logger.error(f"Error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
