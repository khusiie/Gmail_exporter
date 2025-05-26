from gmail_auth import authenticate_gmail
from gmail_fetcher import fetch_emails, get_email_detail, export_to_excel
import pandas as pd  # Import pandas at the top globally

def main():
    service = authenticate_gmail()
    query = input("Enter Gmail search query (e.g., 'has:attachment after:2024/01/01'): ")
    messages = fetch_emails(service, query)

    print(f"Found {len(messages)} messages.")

    all_data = []
    for msg in messages:
        detail = get_email_detail(service, msg['id'], save_folder='attachments')
        all_data.append(detail)

    export_to_excel(all_data, 'emails_export.xlsx')

    # Read and print the Excel file content after exporting
    df = pd.read_excel('emails_export.xlsx')
    print(df)

if __name__ == "__main__":
    main()
