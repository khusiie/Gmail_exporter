📧 Automated Gmail Attachment and Email Data Exporter
A Python application that connects to your Gmail using OAuth2, reads historical emails, extracts attachments, and exports email content + metadata into an Excel file. All attachments are downloaded into structured folders.

📌 Features
🔒 Secure Google OAuth2 Authentication

📥 Fetches all or filtered historical emails (e.g., by date, sender, subject)

📎 Downloads attachments and organizes them by date

📊 Exports email data (sender, recipient, subject, body) to Excel

✅ Simple CLI interface for filtering and control

📂 Project Structure
graphql
Copy
Edit
gmail_exporter/
│
├── email_exporter.py        # Main script to run the exporter
├── gmail_auth.py            # Handles OAuth2 authentication
├── gmail_fetcher.py         # Fetching logic for emails and attachments
├── token.json               # Stores user's OAuth access/refresh token
├── credentials.json         # Google OAuth client credentials
├── attachments/             # Folder where attachments are saved
├── email_export.xlsx        # Output Excel file
├── requirements.txt         # Python dependencies
└── README.md              # This documentation file


🛠 Requirements
Python 3.7+

Gmail API enabled on your Google Cloud project

credentials.json (OAuth2 client secret)

📦 Installation & Setup
1. Clone the Repository
bash
git clone https://github.com/yourusername/gmail-exporter.git
cd gmail-exporter

3. Install Dependencies
bash
pip install -r requirements.txt

5. Set Up Google OAuth2
Go to the Google Cloud Console.

Enable the Gmail API.

Create OAuth 2.0 Client ID credentials.

Download the credentials.json file and place it in the project directory.

🚀 Run the Application
bash
Copy
Edit
python email_exporter.py
You’ll be asked to log in to your Gmail account the first time (a browser window will open).

After authentication, you'll be prompted to enter a Gmail search query, such as:

bash
Copy
Edit
has:attachment after:2024/01/01 before:2024/05/01
✅ This fetches all emails within the date range that contain attachments.

⏹ How to Stop the Script
If you want to interrupt the program while it's running (e.g., during email fetching):

bash
Copy
Edit
Press Ctrl + C
This sends a KeyboardInterrupt and exits the script safely.

📁 Output
✅ email_export.xlsx: Contains structured email data:

Date

Sender

Recipient

Subject

Body

Attachment File Names (if any)

✅ attachments/YYYY-MM-DD/: Folder structure for downloaded attachments.

🔐 Security Notes
OAuth tokens are stored in token.json securely (do not share this file).

No passwords or sensitive data are stored in plain text.

You can revoke access from your Google Account Security page.

✅ Example Output
Date	Sender	Recipient	Subject	Body (Excerpt)	Attachments
2024-01-15	invoice@abc.com	your@email.com	Invoice Jan	Please find invoice	invoice.pdf

💡 Future Enhancements (Optional)
GUI using Tkinter or PyQt

Export to CSV or JSON

Email threading support

Filtering by unread/read/starred

📄 License
MIT License

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.
