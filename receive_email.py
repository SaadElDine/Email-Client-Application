import imaplib
import email
from email.header import decode_header

def receive_email(email_address, password):
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, password)
    mail.select("inbox")

    # Search for the latest email
    result, data = mail.search(None, "ALL")
    latest_email_id = data[0].split()[-1]

    # Fetch the email
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]

    # Parse the email message
    message = email.message_from_bytes(raw_email)

    # Extract the email body
    body = ""
    if message.is_multipart():
        for part in message.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            try:
                body += part.get_payload(decode=True).decode()
            except:
                pass
    else:
        body = message.get_payload(decode=True).decode()

    # Close the connection
    mail.close()
    mail.logout()

    return body

