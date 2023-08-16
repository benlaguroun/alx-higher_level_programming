#!/usr/bin/python3

def subtract_from_max(max_value, values):
    total_to_subtract = sum(value for value in values if value < max_value)
    return max_value - total_to_subtract

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    values_to_subtract = []

    for ch in roman_string:
        value = roman_numerals.get(ch, 0)
        if value > prev_value:
            total += subtract_from_max(value, values_to_subtract)
            values_to_subtract = []
        else:
            values_to_subtract.append(value)
        
        prev_value = value
    
    total += subtract_from_max(prev_value, values_to_subtract)
    return total

# Example usage
roman_number = "MCMXCIV"
print(roman_to_int(roman_number))  # Output should be 1994
