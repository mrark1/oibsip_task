
# 🌦️ Weather Flask App

A simple and elegant weather web application built using **Flask**. This app allows users to search for current weather conditions of any city using real-time data from the OpenWeatherMap API.

## 🚀 Features

- Search weather by city name
- Displays:
  - Temperature (in Celsius)
  - Weather condition (e.g., Clear, Rain, etc.)
  - Humidity
  - Wind Speed
  - Country and City name
- Clean and responsive UI using HTML, CSS, and Bootstrap
- Real-time weather data from OpenWeatherMap API

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS ,JavaScript
- **API**: OpenWeatherMap

## 📦 Installation

1. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your OpenWeatherMap API Key**

   Create a `.env` file or update `app.py` with your API key:
   ```python
   API_KEY = "your_openweathermap_api_key"
   ```

4. **Run the app**
   ```bash
   flask run
   ```

5. **Open in browser**
   Visit: `http://127.0.0.1:5000/`

## 🖼️ Screenshots

![alt text](image.png)

## 🌐 Deployment

This app can be easily deployed on platforms like **Heroku**, **Render**, or **Vercel** using Docker or gunicorn.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙌 Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the free weather API.
- Flask documentation and the Python community for continuous support.









































# BMI Calculator Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A Python application that calculates Body Mass Index (BMI) with both command-line and graphical interfaces, featuring history tracking and unit conversion capabilities.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Functionality
- Calculate BMI from weight and height inputs
- Classify results into standard categories:
  - Underweight (BMI < 18.5)
  - Normal weight (18.5 ≤ BMI < 25)
  - Overweight (25 ≤ BMI < 30)
  - Obese (BMI ≥ 30)

### Command Line Interface (CLI)
- Simple text-based interface
- Immediate results display
- Input validation

### Graphical User Interface (GUI)
- User-friendly Tkinter interface
- Clear input fields and result display
- Error handling with popup messages

### Advanced Features
- Calculation history tracking (saved to JSON)
- Unit conversion (kg/lb and m/ft)
- Color-coded results based on BMI category
- Responsive design that works on different screen sizes

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Video Explanation 
https://drive.google.com/file/d/1KtrjzjQsgVilxRo880CKMVGTeJXqlWI7/view?usp=sharing














































# Advanced Password Generator

![Password Generator Screenshot](screenshot.png)

An advanced password generator application with GUI built using Python and Tkinter. This tool helps create secure, random passwords with customizable options.

## Features

- Generate random passwords with customizable length (8-50 characters)
- Select which character types to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Symbols (!@#$%^&* etc.)
- Exclude specific characters
- Password strength meter with visual feedback
- Copy generated passwords to clipboard
- Save passwords to history for later reference
- Load previously generated passwords from history
- Clean, intuitive user interface

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- pyperclip (`pip install pyperclip`)

## Installation

1. Clone this repository or download the ZIP file
2. Install the required packages:






## Usage

1. Adjust the password length using the slider
2. Select which character types to include
3. (Optional) Enter characters to exclude in the "Exclude Characters" field
4. Click "Generate Password" to create a new password
5. Use the buttons to:
- Copy the password to clipboard
- Save the password to history
- Load a previously saved password
- Delete passwords from history

## Password Strength Meter

The application includes a password strength meter that evaluates:
- Password length
- Character variety (uppercase, lowercase, digits, symbols)
- Provides visual feedback (red/yellow/green) and a percentage score

## Security Notes

- Passwords are generated locally on your machine
- Password history is stored in a JSON file (`password_history.json`)
- For maximum security, consider clearing the password history regularly
- The application uses Python's `secrets` module (through `random`) for cryptographic-quality random number generation

### Video 
https://drive.google.com/file/d/1h18V65yexbswX8Cs6tE-UppCX2AtHvfz/view?usp=sharing

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.