import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example usage
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


# logging to a file

logging.basicConfig(filename='logg.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


try:
    raise ValueError
    
except Exception as e:
    logging.error(f"an error occured, {e}", exc_info=True) # prints stack trace
    



# A stack trace, also known as a traceback, is a report of the active stack frames at a particular point in the execution of a program. 
# It provides information about the sequence of function calls that led to an exception or an error. The stack trace is a valuable diagnostic tool for identifying the cause of a problem in a program.
# Here are the key components of a typical stack trace:

# Function Calls:
# Each line in the stack trace represents a function call. The top of the stack trace is the most recent function call, and it descends to the root cause of the error.
# File and Line Numbers:
# The stack trace usually includes file names and line numbers where each function call occurred. This information helps pinpoint the location of the error in the source code.
# Exception Type and Message:
# If an exception occurred, the stack trace includes the type of the exception and an associated error message. This information is crucial for understanding the nature of the error.




# load logging config from a file
    
from logging.config import fileConfig

# Load the configuration from the file
fileConfig('logging_config.ini')

# Example usage
logging.debug('This is a debug message')
logging.info('This is an info message')
