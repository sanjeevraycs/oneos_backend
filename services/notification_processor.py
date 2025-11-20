import requests
from db.mongodb import db

def auto_save_documents(notification):
    text = notification["content"]

    if ".pdf" in text:
        url = text[text.index("http"):]
        file_data = requests.get(url).content

        db["documents"].insert_one({"file": file_data, "type": "pdf"})
