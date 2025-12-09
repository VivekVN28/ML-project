import sys
from src.logger import logging
def error_message_detail(error, error_detail: sys):
    """
    Generate a detailed error message including the filename and line number
    where the error occurred.

    Args:
        error (Exception): The exception object.
        error_detail (sys): The sys module to access exception info.

    Returns:
        str: A detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in file: {filename} at line: {line_number} | Error message: {str(error)}"

class CustomException(Exception):
    """
    A custom exception class that extends the base Exception class to include
    detailed error information.

    Attributes:
        error_message (str): The detailed error message.
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Initialize the CustomException with a detailed error message.

        Args:
            error_message (str): The original error message.
            error_detail (sys): The sys module to access exception info.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        Return the detailed error message when the exception is converted to a string.

        Returns:
            str: The detailed error message.
        """
        return self.error_message
    
