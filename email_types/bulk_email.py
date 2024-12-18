import csv,time,smtplib
from email_types.simple_email import simple_email

def bulk_email(sender,recievers_path,password,title,body,paths=""):
    try:
        with open(recievers_path,'r') as file:
            getters=csv.DictReader(file)
            reciever=[row["email"] for row in getters]
        server = smtplib.SMTP('smtp.gmail.com',port=587)
        server.starttls()
        server.login(sender,password)
        for rec in reciever:
            msg=simple_email(sender,rec,password,title,body,paths,bulk=True)
            server.sendmail(sender,rec,msg.as_string())
            print("Email Sent Successfully to: ",rec)
            time.sleep(2)
    except Exception as e:
        print(f"Error occured: {e}")