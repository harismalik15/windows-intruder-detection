Windows Intruder Detection System

A security-focused Python application that automatically detects failed Windows login attempts, captures an intruder image via the laptop webcam, encrypts the captured image, and emails it securely to the system owner.

This project is designed around Windows security best practices by leveraging Windows Event Viewer logs rather than attempting to intercept passwords directly.

Features

Detects failed Windows login attempts (Event ID: 4625)

Triggers after a configurable number of failures (default: 2 attempts)

Silently captures an intruder image using the webcam

Encrypts the captured image using AES (Fernet)

Sends the encrypted image via email

Deletes unencrypted images automatically

Runs silently in the background

Supports Windows 10 and Windows 11

Requirements
Operating System

Windows 10 / Windows 11

Administrator privileges (required to read Security Event Logs)

Python Version

Python 3.8 or later


Required Libraries

Install all dependencies using pip:
pip install opencv-python cryptography pywin32


Project Structure
Windows-Intruder-Detection/
│
├── intruder_windows.py # Main detection script
├── crypto_utils.py # AES encryption utilities
├── email_alert.py # Email alert module
├── secret.key # Encryption key (DO NOT SHARE)
├── captures/ # Temporary capture directory
└── README.md


Setup Instructions
Step 1: Generate Encryption Key (Run Once)
from crypto_utils import generate_key
generate_key()

This creates a secret.key file used for encryption and decryption.

⚠️ Do not upload this file to GitHub or share it publicly.


Step 2: Configure Email Alerts

Edit email_alert.py:
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_gmail_app_password"

Gmail Setup

Enable 2-Step Verification

Generate an App Password

Use the app password in the script

Step 3: Run the System

Run the script as Administrator:

python intruder_windows.py

The system will now monitor failed login attempts in the background.

Auto-Start on System Boot (Recommended)
Using Task Scheduler

Open Task Scheduler

Create a new task

Enable Run with highest privileges

Trigger: At startup

Action:
Program: python.exe
Arguments: intruder_windows.py
Start in: project directory


Decrypting Captured Images

Use the following script to decrypt an image:

from cryptography.fernet import Fernet


key = open("secret.key", "rb").read()
fernet = Fernet(key)


with open("intruder.jpg.enc", "rb") as f:
    data = fernet.decrypt(f.read())


with open("intruder.jpg", "wb") as f:
    f.write(data)
Security Notes

The system does not intercept passwords

Uses official Windows Event Viewer logs

Images are encrypted before transmission

Plain images are deleted immediately

Designed to be legal, ethical, and stable

Limitations

Requires Administrator privileges

Webcam must be accessible

Only detects failed login attempts (not successful ones)

Future Enhancements

Short video capture instead of image

Face recognition (known vs unknown)

Cloud storage (Drive / S3)

Auto-lock or shutdown after detection

Multi-email alerts

Disclaimer

This project is intended for personal security and educational purposes only. Do not deploy on systems you do not own or have explicit permission to monitor.

Author

Developed by Muhammad Haris Malik
