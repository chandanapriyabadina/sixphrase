class CustomException(Exception):
    def __init__(self, message):
        self.message = message

# Example usage
try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print("Custom Exception:", e.message)
