# Password Generator

A Python program that generates strong random passwords based on the length entered by the user.

## Features

- User can choose the password length.
- Minimum password length is 4.
- Includes lowercase letters, uppercase letters, numbers, and symbols.
- Ensures at least one lowercase letter, one uppercase letter, one number, and one symbol.
- Uses the `secrets` module for secure random password generation.
- Validates user input and asks again if an invalid length is entered.
- Displays the generated password.
- Asks the user whether to save the generated password to a text file.
- Saves the password to `passwords.txt` when the user chooses `y`.
- Uses functions to keep the code organized and readable.

## Technologies Used

- Python
- `secrets` module
- `random` module
- `string` module

## How to Run

1. Make sure Python is installed on your system.
2. Open the project folder in VS Code.
3. Open the terminal in the project folder.
4. Run the following command:

```bash
python password_generator.py