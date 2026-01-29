#!/usr/bin/env python3
"""
Temperature Converter: Fahrenheit to Celsius with file output
"""
import os
from datetime import datetime

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    output_dir = "/app/logs"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "conversions.txt")
    
    try:
        temp_f = float(input("Enter temperature in Fahrenheit: "))
        temp_c = fahrenheit_to_celsius(temp_f)
        
        result = f"{temp_f}°F = {temp_c:.2f}°C"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Print to console
        print(result)
        
        # Write to file
        with open(output_file, "a") as f:
            f.write(f"[{timestamp}] {result}\n")
        
        print(f"Result saved to {output_file}")
        
    except ValueError:
        print("Error: Please enter a valid number")
        exit(1)

if __name__ == "__main__":
    main()
