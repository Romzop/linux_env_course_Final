#!/usr/bin/env python3
"""
Temperature Converter: Fahrenheit to Celsius
"""

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    try:
        temp_f = float(input("Enter temperature in Fahrenheit: "))
        temp_c = fahrenheit_to_celsius(temp_f)
        print(f"{temp_f}°F = {temp_c:.2f}°C")
    except ValueError:
        print("Error: Please enter a valid number")
        exit(1)

if __name__ == "__main__":
    main()
