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