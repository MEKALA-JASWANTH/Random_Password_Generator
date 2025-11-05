# Random Password Generator

A Python-based random password generator with a modern graphical user interface (GUI) built using Tkinter. This application allows users to generate secure passwords with customizable options and save them for future use.

## Original Features

- Generates random passwords
- Uses Python's random and string modules
- Simple command-line interface

## Features Added by Jaswanth

### 1. **Tkinter GUI Interface**
   - Modern and user-friendly graphical interface
   - Clean layout with organized sections
   - Color-coded buttons for easy navigation
   - Real-time display of generated passwords

### 2. **Customizable Password Length**
   - Adjustable password length from 4 to 50 characters
   - Spinbox control for easy length selection
   - Default length set to 12 characters

### 3. **Multiple Password Generation**
   - Generate 1 to 20 passwords at once
   - All passwords displayed in scrollable text area
   - Useful for creating multiple accounts or backups

### 4. **Character Type Options**
   - **Uppercase Letters (A-Z)**: Include/exclude capital letters
   - **Lowercase Letters (a-z)**: Include/exclude small letters
   - **Numbers (0-9)**: Include/exclude numeric digits
   - **Special Characters**: Include/exclude symbols like !@#$%^&*()
   - Flexible checkbox system for any combination
   - Must select at least one option to generate password

### 5. **Copy to Clipboard**
   - One-click copy functionality
   - Copies all generated passwords to clipboard
   - Uses pyperclip library with fallback method
   - Success confirmation message

### 6. **Save to Text File**
   - Automatically saves passwords to timestamped text file
   - Format: `passwords_YYYYMMDD_HHMMSS.txt`
   - Includes generation timestamp and formatted output
   - File saved in same directory as script
   - Success message shows filename

### 7. **Additional Features**
   - **Clear Display**: Button to clear the password display area
   - **Input Validation**: Error messages for invalid configurations
   - **Scrollable Display**: View multiple passwords with scrollbar
   - **Professional UI**: Color-coded buttons and organized layout

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pyperclip
```

**Note**: Tkinter comes pre-installed with most Python distributions.

## Usage

1. **Run the Application**:
   ```bash
   python Random_Password_Generator.py
   ```

2. **Configure Your Password**:
   - Set desired password length (4-50 characters)
   - Choose number of passwords to generate (1-20)
   - Select character types to include (uppercase, lowercase, numbers, special characters)

3. **Generate Passwords**:
   - Click "Generate Password(s)" button
   - View generated passwords in the display area

4. **Use Your Passwords**:
   - Click "Copy to Clipboard" to copy all passwords
   - Click "Save to File" to store passwords in a text file
   - Click "Clear" to remove passwords from display

## Screenshots

The GUI includes:
- Password length selector
- Number of passwords selector
- Character type checkboxes
- Generate button
- Password display area with scrollbar
- Action buttons (Copy, Save, Clear)

## File Structure

```
Random_Password_Generator/
│
├── Random_Password_Generator.py   # Main application file
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── passwords_*.txt                 # Generated password files (created when saving)
```

## Security Notes

- Passwords are generated using Python's `random` module
- For cryptographic purposes, consider using `secrets` module
- Generated password files are stored locally
- Always store password files securely
- Consider encrypting password files for sensitive data

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- pyperclip==1.8.2

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available for educational purposes.

## Author

- **Original**: biophilic16
- **Enhanced by**: MEKALA-JASWANTH

## Acknowledgments

- Original repository by biophilic16
- Enhanced with GUI and additional features by Jaswanth
