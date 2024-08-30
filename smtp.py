import smtplib
import getpass
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Job:
    def __init__(self, args: dict):
        self.sender = args["sender"]
        self.receiver = args["receiver"]
        self.file = os.path.abspath(args["file"])
        self.senderdomain = self.sender.split('@')[1].split('.com')[0]
        try:
            self.password = getpass.getpass(prompt="Enter senders password: ")
        except Exception as Error:
            print("Error: ", Error)
            os.abort()

    def read_file(self):
        with open(self.file, 'r') as f:
            self.filecontent = f.read()
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = self.receiver
            msg.attach(MIMEText(self.filecontent, 'plain'))
            self.readyobj = msg.as_string()

    def get_host_and_port(self):
        dictionary = dict( gmail=(587, 'smtp.gmail.com'), 
                          outlook=(587, 'smtp-mail.outlook.com'),
                          hotmail=(587, 'smtp-mail.outlook.com'),
                          yahoo=(587, 'smtp.mail.yahoo.com'))

        return dictionary[self.senderdomain]

    def connect(self):
        PORT, HOST = self.get_host_and_port()
        try:
            server = smtplib.SMTP( HOST, PORT)
            statuscode, response = server.ehlo()
            print(f"[*] Echoing the server: {statuscode} {response}")
            statuscode, response = server.starttls()
            print(f"[*] Starting TLS connection: {statuscode} {response}")
            statuscode, response = server.login(self.sender, self.password)
            print(f"[*] Logging in : {statuscode} {response}")
            self.read_file()
            server.sendmail(self.sender, self.receiver, self.readyobj)
        except Exception as Error:
            print("Error: ", Error)
        finally:
            print("Email sent successfully!")
            server.quit()
