# 📧 Gmail Email Exporter

Automated Gmail Attachment and Email Data Exporter is a Python-based utility designed to streamline the process of retrieving and organizing email data from Gmail accounts. Using secure OAuth2 authentication, the tool connects to a user’s Gmail, reads historical emails, and extracts metadata such as date, sender, recipient, subject, and body content. It intelligently filters emails based on customizable criteria (e.g., date range, sender, keywords, attachments), downloads any attachments, and exports the processed data to an Excel file.

---



## 🚀 Features

- 🔍 Search Gmail using custom queries (e.g., `from:someone@example.com`, `has:attachment`, `after:2024/01/01`)
- 📥 Export emails as `.eml` or plain text
- 💾 Save messages locally with structured filenames
- 🔐 OAuth 2.0 authentication with token caching
- 🛠️ Simple and customizable script

---

## 📸 Demo

```bash
$ python email_exporter.py
Enter Gmail search query (e.g., 'has:attachment after:2024/01/01'): from:aman@zninterview.com
Exporting 5 emails...
✔ Email from aman@zninterview.com - Saved as 2025-05-01_Interview_Confirmation.eml
✔ Done!
```
🧰 Requirements
Python 3.7+

Gmail account with API access

Installed libraries:

google-api-python-client

google-auth-httplib2

google-auth-oauthlib

```bash
pip install -r requirements.txt
```

🛠️ Setup Instructions
Enable Gmail API:

Visit the Google Developers Console

Create a new project and enable Gmail API

Generate OAuth credentials (credentials.json) and place it in the same folder as the script

Run the script:

```bash
python email_exporter.py
```

Authenticate once via browser. It will save your token in token_gmail_v1.pickle for future runs.

🔎 Gmail Search Query Examples

Query	Description
from:boss@example.com	Emails from your boss
has:attachment	Emails that include attachments
after:2024/01/01 before:2024/12/31	Emails between specific dates
subject:"Interview Update"	Emails with a specific subject
label:important	Emails marked as important

📂 Output
Emails are saved in the following format:

text
📁 exported_emails/
   ├── 2025-05-01_Interview_Confirmation.eml
   └── 2025-05-03_Feedback_Response.eml

🧑‍💻 Author
Khushi Gupta


🙌 Acknowledgements
Google for providing easy-to-use APIs

The Python open-source community

