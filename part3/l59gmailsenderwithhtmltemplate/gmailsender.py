import smtplib
from email.message import EmailMessage
from datetime import datetime

class GmailSender:
     def __init__(self,senderemail,apppassword):
          self.senderemail = senderemail
          self.apppassword = apppassword
          self.smtpserver = "smtp.gmail.com" # Simple Mail Transfer Protocol
          self.smtpport = 465

     def send(self,toemail,subject,htmlcontent):
          htmlcontent = htmlcontent.substitute({"name":"Mon Mon"})

          msg = EmailMessage()
          msg['From'] = self.senderemail
          msg['To'] = toemail
          msg['Subject'] = subject

          # Plain text
          msg.set_content(htmlcontent)

          # html content 
          msg.add_alternative(htmlcontent,subtype="html")

          try:
               with smtplib.SMTP_SSL(self.smtpserver,self.smtpport) as smtp:
                    smtp.login(self.senderemail,self.apppassword)
                    smtp.send_message(msg)
                    print(f"{datetime.now()} Email send to {toemail}")
          except Exception as err:
               print(f"Error sending email: {err}")
