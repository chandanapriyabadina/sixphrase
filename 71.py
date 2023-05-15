def divide_by_zero():
    try:
        result = 5 / 0
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage
divide_by_zero()
