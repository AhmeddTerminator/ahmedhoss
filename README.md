# Lorem Encryptor GUI

## Overview
Lorem Encryptor is a Python application that allows users to encrypt and decrypt messages using a unique mapping of letters A-Z to corresponding Lorem Ipsum-style words. The application features a user-friendly graphical interface built with Tkinter, making it easy to use for anyone.

## Project Structure
```
lorem-encryptor-gui/
├── src/
│   ├── Encrypt.py        # Contains the encryption functionality
│   ├── decrypt.py        # Implements the decryption functionality
│   ├── gui.py            # Creates the graphical user interface
│   └── utils.py          # Contains utility functions
├── requirements.txt       # Lists the project dependencies
└── README.md              # Documentation for the project
```

## Installation
To get started with the Lorem Encryptor GUI, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd lorem-encryptor-gui
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/gui.py
   ```

2. The GUI will open, allowing you to input text for encryption or decryption.

3. Enter the text you want to encrypt or decrypt and click the corresponding button to see the results.

## Features
- Encrypt messages by replacing letters with Lorem Ipsum-style words.
- Decrypt messages back to their original form.
- User-friendly interface for easy interaction.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.