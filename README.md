
# 🔐 Password Strength Checker

## About the Project

Password Strength Checker is a beginner-friendly Python project
that analyzes a password and estimates its strength based on
basic security rules.

It checks password length, character types, and whether the
password matches a small list of commonly used passwords.

The program provides a strength score and suggestions to help
users improve their passwords.

## Features

- Checks password length.
- Detects uppercase and lowercase letters.
- Detects numbers and special characters.
- Checks against a small list of common passwords.
- Calculates a password strength score.
- Provides suggestions for improvement.

## Technologies Used

- Python
- Regular Expressions (re)
- Python Functions
- Lists, Sets, and Dictionaries
- Conditional Statements and Loops

## Project Structure

PasswordStrengthChecker/
├── password_checker.py
├── main.py
└── README.md

## Requirements

- Python 3 installed on your computer.
- A code editor or terminal.

## How to Run

1. Open the project folder in your terminal.
2. Run the following command:

   python3 main.py

3. Enter a sample password when prompted.
4. Review the strength score and suggestions.

## Example

Input:
River!Cloud82

The program evaluates the password and displays its
estimated strength, score, and any suggestions.

The result depends on the checks implemented in
password_checker.py.

## Learning Objectives

This project demonstrates:

- Python functions and modules.
- String handling.
- Regular expressions.
- Sets, lists, and dictionaries.
- Conditional logic.
- Basic password-strength evaluation.

## Limitations

This project uses a simple scoring system and a small list
of common passwords. It does not guarantee that a password
is secure or estimate its actual resistance to guessing.

The program does not store or transmit passwords in its
current implementation.

## Future Improvements

- Add a graphical user interface using Tkinter.
- Expand the common-password checks.
- Improve strength estimation.
- Add automated tests.

## Author

Created as a Python learning project.
