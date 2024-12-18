import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_types.attach_files import attach_files

def simple_email(sender,reciever,password,title,body,paths="",bulk=False):
    if not paths:
        msg=MIMEText(body,"plain")
        msg["From"]=sender
        msg["To"]=reciever
        msg["Subject"]=title
    else:
        msg=MIMEMultipart()
        msg["From"]=sender
        msg["To"]=reciever
        msg["Subject"]=title
        msg.attach(MIMEText(body,"plain"))
        attachment_files=attach_files(paths)
        for file in attachment_files:
            msg.attach(file)
    if not bulk:
        try:
            server = smtplib.SMTP('smtp.gmail.com',port=587)
            server.starttls()
            server.login(sender,password)
            server.sendmail(sender,reciever,msg.as_string())
            print("Email Sent Successfully to: ",reciever)
        except Exception as e:
            print("Error occured: ",e)
        finally:
            server.close()
    else:
        return msg