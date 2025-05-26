
# 📧 Automated Gmail Attachment and Email Data Exporter

A secure and efficient Python application that connects to a Gmail account via OAuth2, fetches historical emails with filter options, extracts metadata, downloads attachments, and exports the data to an Excel file. Attachments are organized in structured folders.

---

## 🎯 Objective

Build a reliable tool to automate the following:
- Access Gmail using OAuth2.
- Fetch all or filtered historical emails.
- Extract metadata and email content.
- Download attachments.
- Export data to an Excel spreadsheet.
- Organize attachments by date.

---

## 🛠️ Key Features

### 1. 🔐 Gmail Access & Authentication
- Secure authentication via **Google OAuth2**.
- Minimal permission scope (`gmail.readonly` or `gmail.modify`) for privacy and security.
- OAuth tokens are saved securely (`token.json`).

### 2. 📬 Email Fetching
- Supports reading from inbox, sent mail, etc.
- Flexible filter options:
  - **Date range** (last 30 days or custom).
  - **Sender/Recipient** email.
  - **Subject** keywords.
  - **Attachments-only** option.

### 3. 📎 Attachment Handling
- Detect and download all email attachments.
- Save them in structured format:


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
