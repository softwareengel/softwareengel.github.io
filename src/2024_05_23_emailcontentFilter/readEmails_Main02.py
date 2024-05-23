import imaplib
import email
from email.header import decode_header
import os
import re
from collections import Counter
import matplotlib.pyplot as plt


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

def extract_text_from_email(msg):
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if (  content_type == "text/plain" or content_type == "text/html")  and "attachment" not in content_disposition:
                try:
                    body += part.get_payload(decode=True).decode()
                except Exception as e:
                    print(f"Could not decode part: {e}")
    else:
        content_type = msg.get_content_type()
        if content_type == "text/plain" or content_type == "text/html":
            try:
                body += msg.get_payload(decode=True).decode()
            except Exception as e:
                print(f"Could not decode part: {e}")
    return body

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
            
def extract_ip_from_subject(subject, v4= True , v6 = True):
    # Regex pattern for matching IPv4 addresses
    ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    # Regex pattern for matching IPv6 addresses
    ipv6_pattern = r'\b(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}\b|\b(?:[A-F0-9]{1,4}:){1,7}:[A-F0-9]{1,4}\b'
    ipv4_addresses = re.findall(ipv4_pattern, subject, re.IGNORECASE)
    ipv6_addresses = re.findall(ipv6_pattern, subject, re.IGNORECASE)
    ret =[]
    if v4:
        ret +=   ipv4_addresses
    if v6:
        ret += ipv6_addresses
    return ret

def get_ip_addresses_from_subjects(emails):
    all_ip_addresses = []
    for msg in emails:
        subject, encoding = decode_header(msg.get("Subject"))[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
        ip_addresses = extract_ip_from_subject(subject, v4=True, v6=False    )
        if ip_addresses:
            print("Subject:", subject)
            print("IP Addresses:", ip_addresses)
            print()
            all_ip_addresses += ip_addresses
    return all_ip_addresses

def plot_histogram(ip_addresses):
    # Count occurrences of each IP address
    ip_counter = Counter(ip_addresses)
    ips, counts = zip(*ip_counter.items())

    # Create the histogram
    plt.figure(figsize=(10, 5))
    plt.bar(ips, counts, color='blue')
    plt.xlabel('IP Addresses')
    plt.ylabel('Counts')
    plt.title('Histogram of IP Addresses')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('ip_histogram.png')
    plt.show()
    
def main():
    credentials = read_credentials('credentials.txt')
    mail = connect_to_imap(credentials)
    folder = 'Logs'  # Replace with your subfolder name

    subject_keyword = 'Internet-Adresse:'  # Replace with the subject keyword to filter
    email_ids = fetch_emails(mail, folder=folder, search_criterion='ALL')
    filtered_emails = filter_emails_by_subject(mail, email_ids, subject_keyword)
    print_emails(filtered_emails)
    ipadresses = get_ip_addresses_from_subjects(filtered_emails)
    print(ipadresses)
    plot_histogram(ipadresses)

    # subject_keyword = 'Verbindungsdaten'  # Replace with the subject keyword to filter
    # email_ids = fetch_emails(mail, folder=folder, search_criterion='ALL')
    # filtered_emails = filter_emails_by_subject(mail, email_ids, subject_keyword)
    # write_emails_to_file(filtered_emails, 'filtered_emails.txt')
    mail.logout()

if __name__ == "__main__":
    main()
