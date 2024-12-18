====Email Sender Project====
This project allows you to send emails using Python, with support for sending simple emails, bulk emails, and emails with attachments. It is designed specifically for Gmail.

====Features====
Simple Email Sender: Send a basic email with subject and body content to a single recipient.
Bulk Email Sender: Send the same email to multiple recipients with a CSV file.
Email with Attachments: Attach files (e.g., images, PDFs) to your emails.

====Requirements====
Python 3.7 or higher
A Gmail account (for sending emails)

====Setup Instructions====
Download or Copy the Project Files: Download or copy the source files for the Email Sender project to your computer.

Install Dependencies: Make sure you have Python 3.7 or higher installed.

====Set Up Gmail App Password====
Go to your Google Account Security settings.
Enable 2-Step Verification if it’s not already enabled.
Under "Signing in to Google," select App Passwords.
Choose "Mail" for the app, and "Other (Custom name)" for the device (e.g., "Email Sender").
Generate the app password and keep it for later use.

====Running the Program====
Open the terminal or command prompt in your project folder and run the program using:
bash
Copy code
python main.py

====Example File Paths====
For attachments: If you want to attach a file, specify the full file path. For example:

C:\Users\YourName\Documents\report.pdf (on Windows)
/Users/YourName/Documents/report.pdf (on macOS or Linux)
For the bulk email CSV file: The CSV file should have a column of email addresses. It should have an email column the rest does'nt matter. Example CSV format:

csv
Copy code
email,name
email1@example.com,name1
email2@example.com,name2
email3@example.com,name3

You can place the CSV file in the same folder as your script, or specify the full path to the file (e.g., C:\Users\YourName\email_list.csv).

====How the Program Works====
Simple Email: You can set the recipient's email address, subject, and body directly in the script.
Bulk Email: If you have a CSV file with email addresses, the script will send the email to each address listed in the file.
Attachments: You can specify file paths to attach files to your emails.
Notes
Only Gmail accounts are supported for sending emails in this project.
Ensure that attachments exist and the file paths are correct before running the script.
Make sure the CSV file with email addresses is formatted properly and contains valid email addresses.

====Advanced Features====
If you need more advanced features, such as scheduling emails, HTML emails, or support for other email providers, please contact me either through LinkedIn: https://www.linkedin.com/in/asad-sagheer786 or Fiverr: https://www.fiverr.com/asadsagheer786 for custom solutions.

====License====
This project is open source and available under the MIT License.