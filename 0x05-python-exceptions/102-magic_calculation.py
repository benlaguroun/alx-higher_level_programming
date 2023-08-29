#!/usr/bin/python3

def magic_calculation(a, b):
    try:
        if a > b:
            result = a ** b / (a - b)
        else:
            result = a + b
    except ZeroDivisionError:
        result = "Division by zero is not allowed."
    except Exception as e:
        result = f"An error occurred: {str(e)}"

    return (result)
