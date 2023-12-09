
# THIS IS MY CUSTOM EXCEPTION FILE
import sys


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() # It returns a tuple (exc_type, exc_value, exc_traceback)

    # exc_traceback refers to the traceback object associated with an exception. 
    # When an exception occurs, Python generates a traceback that contains information
    #  about the call stack at the time the exception was raised. 
    # This traceback includes details such as the file name, line number, and
    #  function calls leading up to the point where the exception occurred.

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message


class AppException(Exception): # Inherited from Python Exception Class
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message