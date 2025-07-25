import sys
import os
from datetime import datetime

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        exc_type, exc_obj, exc_tb = error_details.exc_info()
        self.error_message = error_message
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in Python script [{0}] at line [{1}]: {2}".format(
            self.file_name, self.lineno, str(self.error_message)
        )

def log_error_to_file(message: str):
    # Define logs directory path relative to this file
    logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
    os.makedirs(logs_dir, exist_ok=True)  # Create 'logs' directory if it doesn't exist

    log_file_path = os.path.join(logs_dir, 'networksecurity.log')

    with open(log_file_path, 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

if __name__ == "__main__":
    try:
        print("Enter the try block")
        a = 1/0
        print("This will not be printed", a)
    except Exception as e:
        custom_exception = NetworkSecurityException(e, sys)
        log_error_to_file(str(custom_exception))
        raise custom_exception  # Optional: Raise if you want it to propagate after logging
