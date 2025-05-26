"""
bmi_calculator/utils.py

Utility functions for the BMI Calculator project.
"""

import json
import os
from datetime import datetime
from typing import Union, Optional, Dict, List

# Constants
DEFAULT_HISTORY_FILE = "bmi_history.json"
VALID_CATEGORIES = ["Underweight", "Normal weight", "Overweight", "Obese"]

def validate_input(weight: Union[str, float], height: Union[str, float]) -> tuple:
    """
    Validate user input for weight and height.
    
    Args:
        weight: User's weight input (kg)
        height: User's height input (meters)
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    try:
        weight_float = float(weight)
        height_float = float(height)
        
        if weight_float <= 0 or height_float <= 0:
            return False, "Weight and height must be positive numbers"
            
        if height_float > 3:  # Unrealistically tall
            return False, "Please enter height in meters (e.g., 1.75)"
            
        if weight_float > 500:  # Unrealistically heavy
            return False, "Please enter weight in kilograms"
            
        return True, ""
        
    except ValueError:
        return False, "Please enter valid numbers for weight and height"

def save_to_history(
    bmi_data: Dict[str, Union[float, str]],
    filename: str = DEFAULT_HISTORY_FILE
) -> bool:
    """
    Save BMI calculation to history file.
    
    Args:
        bmi_data: Dictionary containing:
            - weight: float
            - height: float
            - bmi: float
            - category: str
            - timestamp: str (optional)
        filename: Path to history file
        
    Returns:
        bool: True if save was successful
    """
    try:
        # Add timestamp if not provided
        if "timestamp" not in bmi_data:
            bmi_data["timestamp"] = datetime.now().isoformat()
        
        history = load_history(filename)
        history.append(bmi_data)
        
        with open(filename, "w") as f:
            json.dump(history, f, indent=2)
            
        return True
        
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error saving history: {e}")
        return False

def load_history(filename: str = DEFAULT_HISTORY_FILE) -> List[Dict]:
    """
    Load BMI calculation history from file.
    
    Args:
        filename: Path to history file
        
    Returns:
        List of BMI records (dictionaries)
    """
    try:
        if os.path.exists(filename):
            with open(filename, "r") as f:
                return json.load(f)
        return []
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading history: {e}")
        return []

def clear_history(filename: str = DEFAULT_HISTORY_FILE) -> bool:
    """
    Clear the BMI calculation history.
    
    Args:
        filename: Path to history file
        
    Returns:
        bool: True if operation was successful
    """
    try:
        if os.path.exists(filename):
            os.remove(filename)
        return True
    except IOError as e:
        print(f"Error clearing history: {e}")
        return False

def convert_units(
    value: float,
    from_unit: str,
    to_unit: str
) -> Optional[float]:
    """
    Convert between different units (kg/lb, meters/feet).
    
    Args:
        value: Value to convert
        from_unit: Original unit ('kg', 'lb', 'm', 'ft')
        to_unit: Target unit ('kg', 'lb', 'm', 'ft')
        
    Returns:
        Converted value or None if conversion not possible
    """
    conversions = {
        'kg': {'lb': lambda x: x * 2.20462},
        'lb': {'kg': lambda x: x / 2.20462},
        'm': {'ft': lambda x: x * 3.28084},
        'ft': {'m': lambda x: x / 3.28084}
    }
    
    try:
        return conversions[from_unit][to_unit](value)
    except KeyError:
        return None

def format_bmi_result(bmi: float, category: str) -> str:
    """
    Format BMI results for display.
    
    Args:
        bmi: Calculated BMI value
        category: BMI category string
        
    Returns:
        Formatted string with BMI and category
    """
    return f"BMI: {bmi:.2f}\nCategory: {category}"

def get_category_color(category: str) -> str:
    """
    Get color associated with BMI category for GUI display.
    
    Args:
        category: BMI category string
        
    Returns:
        Color name (for Tkinter) or hex code
    """
    colors = {
        "Underweight": "lightblue",
        "Normal weight": "lightgreen",
        "Overweight": "orange",
        "Obese": "lightcoral"
    }
    return colors.get(category, "white")