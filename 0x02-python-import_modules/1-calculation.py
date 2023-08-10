#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, product, and quotient of 10 and 5."""  # Updated comment
    
    # Importing functions directly from the module
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Printing the results using f-strings (Python 3.6+)
    print(f"{a} + {b} = {add(a, b)}")  # Using f-string
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
