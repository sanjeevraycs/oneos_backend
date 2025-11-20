from imapclient import IMAPClient
from pyzmail import PyzMessage
from db.mongodb import emails_col

def fetch_gmail(username, app_password):
    HOST = "imap.gmail.com"
    with IMAPClient(HOST) as client:
        client.login(username, app_password)
        client.select_folder("INBOX")

        messages = client.search(["UNSEEN"])

        for msgid, data in client.fetch(messages, ["RFC822"]).items():
            msg = PyzMessage.factory(data[b"RFC822"])
            email_data = {
                "from": msg.get_address("from")[1],
                "subject": msg.get_subject(),
                "body": msg.text_part.get_payload().decode() if msg.text_part else "",
            }
            emails_col.insert_one(email_data)
