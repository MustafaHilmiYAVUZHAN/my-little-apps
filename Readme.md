# Email Automation and Remote Execution

This Python script automates email sending, receiving, and executing commands remotely based on the subject line of the received email. It's designed to be run as a startup process on Windows systems.

## Features

- Sends connection status email on startup.
- Monitors the inbox for new emails.
- Executes commands based on the subject line of received emails.
- Sends confirmation emails after executing commands.
- Handles errors and sends notifications via email.

## Requirements

- Python 3.x
- Libraries: imaplib, email, time, pyautogui, smtplib, winshell, os, sys, keyboard, requests, browsercookie

## Instructions

1. Ensure Python 3.x is installed on your system.
2. Install the required libraries using pip: `pip install imaplib email pyautogui smtplib requests keyboard`.
3. Set up a Yandex email account to use as the sender and receiver.
4. Update the `username` and `password` variables in the script with your Yandex email credentials.
5. Run the script on your system. It will send a connection status email and start monitoring the inbox.
6. Send emails with commands in the subject line to execute them remotely.
7. Check your inbox for confirmation or error emails after executing commands.