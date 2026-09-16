#!/usr/bin/env python3
"""
Module: main.py
Description: A simple calculator that performs basic arithmetic operations.
Supports addition, subtraction, multiplication, and division.
"""

import sys

def add(a: float, b: float) -> float:
    """Returns the sum of a and b."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Returns the quotient of a divided by b.
    Raises ValueError if b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def get_number(prompt: str) -> float:
    """Gets a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    """Main calculator loop."""
    print("Simple Calculator")
    print("-----------------")
    print("Operations: +  -  *  /")
    print("Type 'quit' to exit.")
    
    while True:
        print()
        operator = input("Enter operator: ").strip().lower()
        
        if operator == "quit":
            print("Goodbye!")
            break
        
        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator. Use +, -, *, or /.")
            continue
        
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        try:
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            else:
                result = divide(num1, num2)
            
            print(f"Result: {num1} {operator} {num2} = {result}")
            
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit()