import tkinter as tk
from tkinter import ttk, messagebox
from .calculator import calculate_bmi, classify_bmi

class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.setup_ui()
        
    def setup_ui(self):
        # Create main frame
        mainframe = ttk.Frame(self.root, padding="20")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        # Weight entry
        ttk.Label(mainframe, text="Weight (kg):").grid(column=0, row=0, sticky=tk.W)
        self.weight = tk.StringVar()
        weight_entry = ttk.Entry(mainframe, width=15, textvariable=self.weight)
        weight_entry.grid(column=1, row=0, sticky=tk.W)
        
        # Height entry
        ttk.Label(mainframe, text="Height (m):").grid(column=0, row=1, sticky=tk.W)
        self.height = tk.StringVar()
        height_entry = ttk.Entry(mainframe, width=15, textvariable=self.height)
        height_entry.grid(column=1, row=1, sticky=tk.W)
        
        # Calculate button
        ttk.Button(
            mainframe, 
            text="Calculate BMI", 
            command=self.calculate
        ).grid(column=0, row=2, columnspan=2, pady=10)
        
        # Results display
        self.result = tk.StringVar()
        self.result.set("Enter your details to calculate BMI")
        ttk.Label(mainframe, textvariable=self.result).grid(column=0, row=3, columnspan=2)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
    def calculate(self):
        try:
            weight = float(self.weight.get())
            height = float(self.height.get())
            
            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive numbers")
                return
                
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
            
            self.result.set(f"BMI: {bmi:.2f}\nCategory: {category}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for weight and height")