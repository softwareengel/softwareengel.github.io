import imaplib
import email
from email.header import decode_header
import os

def read_credentials(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    
    credentials = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, value = line.strip().split('=')
                credentials[name] = value
    except FileNotFoundError:
        print(f"Error: {file_name} not found in the script directory.")
        exit(1)
    return credentials

def connect_to_imap(credentials):
    # Connect to the server
    mail = imaplib.IMAP4_SSL(credentials['imap_host'])
    # Login to the account
    mail.login(credentials['imap_user'], credentials['imap_pass'])
    return mail

def fetch_emails(mail, folder='inbox', search_criterion='ALL'):
    # Select the folder
    status, messages = mail.select(folder)
    if status != 'OK':
        print(f"Error selecting folder {folder}")
        exit(1)
    # Search for emails matching the criterion
    status, messages = mail.search(None, search_criterion)
    if status != 'OK':
        print(f"Error searching emails in folder {folder}")
        exit(1)
    email_ids = messages[0].split()
    return email_ids

def filter_emails_by_subject(mail, email_ids, subject_keyword):
    filtered_emails = []
    for email_id in email_ids:
        # Fetch the email by ID
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        if status != 'OK':
            print(f"Error fetching email ID {email_id}")
            continue
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                # Decode email subject
                subject, encoding = decode_header(msg.get("Subject"))[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                if subject_keyword in subject:
                    filtered_emails.append(msg)
    return filtered_emails

def decode_mime_words(s):
    return ''.join(
        word if isinstance(word, str) else word.decode(encoding or 'utf-8')
        for word, encoding in decode_header(s)
    )

def print_emails(emails):
    for msg in emails:
        subject, encoding = decode_header(msg.get("Subject"))[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
        print("Subject:", subject)
        print("From:", msg.get("From"))
        print("To:", msg.get("To"))
        print("Date:", msg.get("Date"))
        print()

def extract_text_from_email(msg):
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if "attachment" not in content_disposition:
                try:
                    body = part.get_payload(decode=True).decode()
                except:
                    pass
                if content_type == "text/plain":
                    return body

def write_emails_to_file(emails, file_name):
    with open(file_name, 'w') as file:
        for msg in emails:
            subject, encoding = decode_header(msg.get("Subject"))[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else 'utf-8')
            from_ = msg.get("From")
            date = msg.get("Date")
            body = extract_text_from_email(msg)
            file.write(f"Subject: {subject}\n")
            file.write(f"From: {from_}\n")
            file.write(f"Date: {date}\n")
            file.write("Body:\n")
            file.write(body)
            file.write("\n" + "="*40 + "\n")
def main():
    credentials = read_credentials('credentials.txt')
    mail = connect_to_imap(credentials)
    folder = 'Logs'  # Replace with your subfolder name
    subject_keyword = 'Verbindungsdaten'  # Replace with the subject keyword to filter
    email_ids = fetch_emails(mail, folder=folder, search_criterion='ALL')
    filtered_emails = filter_emails_by_subject(mail, email_ids, subject_keyword)
    print_emails(filtered_emails)
    write_emails_to_file(filtered_emails, 'filtered_emails.txt')
    mail.logout()

if __name__ == "__main__":
    main()
