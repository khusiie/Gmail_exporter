# Automated Gmail Attachment and Email Exporter

## Features
- Authenticate securely via OAuth2.
- Fetch emails with filters (date, sender, attachment).
- Download and save attachments in structured folders.
- Export email metadata and content to Excel.

## Setup
1. Clone the repo.
2. Create a project on Google Cloud and enable Gmail API.
3. Download `credentials.json` and place in root.
4. Install dependencies: `pip install -r requirements.txt`
5. Run: `python email_exporter.py`

## Output
- Excel: `email_export.xlsx`
- Folder: `attachments/YYYY-MM-DD/filename.ext`
