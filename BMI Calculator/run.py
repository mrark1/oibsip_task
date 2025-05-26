#!/usr/bin/env python3
"""
BMI Calculator - Main Entry Point

Usage:
    Run without arguments for GUI version:
        python run.py
        
    Run with '--cli' argument for command-line version:
        python run.py --cli
"""

import argparse
from bmi_calculator.calculator import calculate_bmi, classify_bmi
from bmi_calculator.gui import BMICalculatorApp
import tkinter as tk

def run_cli_version():
    """Run the command-line interface version"""
    print("\nBMI Calculator (Command Line Version)")
    print("----------------------------------")
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers")
            return
            
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nResults:")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        
    except ValueError:
        print("Error: Please enter valid numbers for weight and height")

def run_gui_version():
    """Run the graphical user interface version"""
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='BMI Calculator')
    parser.add_argument('--cli', action='store_true', help='Run in command-line mode')
    args = parser.parse_args()

    # Run the appropriate version
    if args.cli:
        run_cli_version()
    else:
        run_gui_version()