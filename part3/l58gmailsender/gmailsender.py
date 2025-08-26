class GmailSender:
     def __init__(self,senderemail,apppassword):
          self.senderemail = senderemail
          self.apppassword = apppassword
          self.smptserver = "smtp.gmail.com" # Simple Mail Transfer Protocol
          self.smtpport = 465

     # def send(self,toemail,subject,cotent):

     # 17GM