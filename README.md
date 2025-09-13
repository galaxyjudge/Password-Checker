# Password Checker Tool

Checks if passwords have been compromised using the [Have I Been Pwned](https://haveibeenpwned.com/) API — and reports exactly how many times each password has been breached.

> 🔒 Never enter real passwords into untrusted tools — this tool is for educational purposes only.

## How It Works

Reads all content from `passwords.txt`, splitting passwords by single spaces (`' '`) only. Sends each password (hashed) to the Have I Been Pwned API. For each password, retrieves the exact number of times it appeared in known data breaches. Reports whether the password was found — and how many times.

Example output:
congratulations!! uendoe has not been pawned
totototo has been pawned 27868 times

Important: Passwords must be separated by a single space character only. Newlines, commas, tabs, or multiple consecutive spaces are not supported — they will cause errors or incorrect parsing.

## How to Use

Install Python (if not installed): https://www.python.org/downloads/

Install the requests library:
py -m pip install requests

Create a file named `passwords.txt` in the same folder as `checkmypass.py`.

Format the file with passwords separated by single spaces only:
password123 totototo mammama keeeke

Do NOT use commas, newlines, or multiple spaces.

Run the script:
py checkmypass.py

You’ll see output like:
congratulations!! #bendoe has not been pawned
totototo has been pawned 27868 times
mammama has been pawned 332 times
keeeke has been pawned 1 times

Interpretation:
- "has not been pawned" means the password was not found in any breach.
- "has been pawned X times" means it was found in X known data leaks. Even one time means it’s compromised.

Pro Tip: Change any password found in a breach — even once.

## Files Included

checkmypass.py — Main script that checks passwords and reports breach counts  
passwords.txt — List of passwords separated by single spaces only

## Security Note

This tool uses k-anonymity via the HIBP API — your full password is never sent. Only the first 5 characters of its SHA-1 hash are transmitted.  
Read more: https://haveibeenpwned.com/API/v3#PwnedPasswords

## License

MIT License — feel free to use, modify, and share!

Copyright (c) 2025 galaxyjudge

Made with ❤️ by galaxyjudge☄️

