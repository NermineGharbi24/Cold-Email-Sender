# Cold Email Sender (NO AI)

<p align="center">
  <img src="/logo.png" alt="Cold Email Sender Logo" width="400"/>
</p>

A Python application designed to automate and streamline the process of sending personalized cold emails with attachments to multiple recipients. Perfect for job applications, networking, or business outreach. Currenlly this project only work by test Users only (max 100) till the verification comes from google. It will get updated later. 

## 🚀 Key Features

- **Automated Email Distribution**: Send personalized emails to multiple recipients at once
- **Smart Personalization**: Automatically extracts recipient names from email addresses
- **Attachment Support**: Easily include resume, cover letter, or other documents
- **Email Tracking**: Logs the status of each sent email
- **Gmail API Integration**: Uses Google's secure API for reliable delivery
- **GDPR Compliant**: Includes unsubscribe options and privacy protection

## 📋 Prerequisites

- Python 3.8+
- Gmail account

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NermineGharbi24/Cold-Email-Sender.git
   cd Cold-Email-Sender
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. **Email Data Setup**:
   - Create `data/contacts.xlsx` with a column named "Email" containing recipient addresses
   - Place your resume (`resume.pdf`) and cover letter (`cover_letter.pdf`) in `data/attachments/`
    -Create `logs/email_log.txt`
    
2. **Google OAuth Setup**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project and enable the Gmail API
   - Configure OAuth Consent Screen (External user type)
   - Create OAuth credentials and download `credentials.json`
   - Place `credentials.json` in the project root directory

## 📤 Usage

1. **Run the Application**:
   ```bash
   python main.py
   ```

2. **Authentication**:
   - First-time use will open a browser window for Google account authentication
   - Grant the necessary permissions to send emails on your behalf

3. **Sending Emails**:
   - Follow the prompts to customize your email subject and body
   - The application will handle the rest, sending emails to all contacts in your list

## 📊 Monitoring

- Check `logs/email_log.txt` for a record of all sent emails
- The log includes timestamps, recipient information, and delivery status

## 🔒 Privacy & Security

- Your Google credentials are stored securely in `token.json` (automatically created)
- No email content or recipient data is stored beyond the local log file
- The application follows email best practices and anti-spam guidelines

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find any issues:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 📧 Contact

Nermine Gharbi - [GitHub Profile](https://github.com/NermineGharbi24)

Project Link: [https://github.com/NermineGharbi24/Cold-Email-Sender](https://github.com/NermineGharbi24/Cold-Email-Sender)