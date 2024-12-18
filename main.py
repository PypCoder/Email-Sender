from email_types.simple_email import simple_email
from email_types.bulk_email import bulk_email

def main():
    print("Welcome to Email Sender!")
    print("Choose an option:")
    print("1. Send a simple email")
    print("2. Send bulk emails")
    print("3. Send email with attachments")
    print("4. Send bulk emails with attachments")

    choice = input("Enter your choice (1/2/3/4): ")
    user_email = input("Enter your email: ")
    password = input("Enter your 16-character password: ")
    if choice == "1":
        recipient = input("Enter recipient email: ")
        subject = input("Enter subject: ")
        message = input("Enter message: ")
        simple_email(user_email,recipient,password,subject,message)
    elif choice == "2":
        file_path = input("Enter path to CSV file with recipient emails: ")
        subject = input("Enter subject: ")
        message = input("Enter message: ")
        bulk_email(user_email,file_path,password,subject,message)
    elif choice == "3":
        recipient = input("Enter recipient email: ")
        subject = input("Enter subject: ")
        message = input("Enter message: ")
        attachment_paths = input("Enter paths to attachments (comma-separated): ").split(",")
        simple_email(user_email,recipient,password,subject,message,paths=attachment_paths)
    elif choice == "4":
        file_path = input("Enter path to CSV file with recipient emails: ")
        subject = input("Enter subject: ")
        message = input("Enter message: ")
        attachment_paths = input("Enter paths to attachments (comma-separated): ").split(",")
        bulk_email(user_email,file_path,password,subject,message,paths=attachment_paths)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        main()