from src.utils.excel_utils import read_contacts
from src.utils.email_utils import extract_name_from_email
from src.email_sender import send_email

def main():
    # Read email addresses from Excel file
    emails = read_contacts("data/contacts.xlsx")
    if emails is None:
        print("Failed to read contacts. Exiting.")
        return

    # Print the emails (for debugging)
    print("Email addresses:", emails)

    # Send emails
    for email in emails:
        recipient_name = extract_name_from_email(email)
        send_email(email, "Your Company", recipient_name)  # Replace "Your Company" with a dynamic value if needed

if __name__ == "__main__":
    main()