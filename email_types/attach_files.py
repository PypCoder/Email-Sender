from email.mime.base import MIMEBase
from email import encoders
import os

def attach_files(filepaths):
    attachments=[]
    for filepath in filepaths:
        if os.path.exists(filepath):
            with open(filepath, 'rb') as attach:
                msg = MIMEBase("application", "octet-stream")
                msg.set_payload(attach.read())
                encoders.encode_base64(msg)
                filename = os.path.basename(filepath)
                msg.add_header("Content-Disposition", f"attachment; filename={filename}")
                attachments.append(msg)
        else:
            print(f"File {filepath} does not found!")
    return attachments