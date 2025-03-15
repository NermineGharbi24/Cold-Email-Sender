import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Paths to attachments
RESUME_PATH = "data/attachments/resume.pdf"
COVER_LETTER_PATH = "data/attachments/cover_letter.pdf"

def authenticate_gmail():
    """Authenticate with Gmail using OAuth."""
    creds = None
    # The file token.json stores the user's access and refresh tokens.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no valid credentials, prompt the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for future use.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def log_email(email, status):
    """
    Log the email sending status to a file.

    Args:
        email (str): The recipient's email address.
        status (str): The status of the email (e.g., "Sent" or "Failed").
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {email} - {status}\n"

    with open("logs/email_log.txt", "a") as log_file:
        log_file.write(log_entry)

def create_message_with_attachments(to, subject, body, attachments):
    """
    Create a message with attachments.

    Args:
        to (str): Recipient email address.
        subject (str): Email subject.
        body (str): Email body.
        attachments (list): List of file paths to attach.

    Returns:
        dict: A message object with attachments.
    """
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = 'me'
    message['subject'] = subject

    # Add the email body
    message.attach(MIMEText(body, 'plain'))

    # Add attachments
    for file_path in attachments:
        part = MIMEBase('application', 'octet-stream')
        with open(file_path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename="{os.path.basename(file_path)}"'
        )
        message.attach(part)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_email(to_email, company_name, recipient_name):
    """
    Send a personalized email to a recipient using the Gmail API.
    """
    try:
        # Authenticate with Gmail
        creds = authenticate_gmail()
        service = build('gmail', 'v1', credentials=creds)

        # Create the email body
        body = f"""
Dear {recipient_name},

I hope this email finds you well. My name is Nermine, and I am reaching out to express my interest in joining {company_name} as a Junior Engineer.

I have attached my resume and cover letter for your review. I would be thrilled to have a chance to join your team.

Thank you for your time and consideration. I look forward to the possibility of discussing this opportunity further.

Best regards,
Nermine.
"""

        # Create the email message with attachments
        attachments = [RESUME_PATH, COVER_LETTER_PATH]
        message = create_message_with_attachments(to_email, f"Job Application - {company_name}", body, attachments)

        # Send the email
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        print(f"Email sent to {to_email}")
        log_email(to_email, "Sent")  # Log successful email
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")
        log_email(to_email, f"Failed: {e}")  # Log failed email