from gmailsender import GmailSender
from string import Template 
from pathlib import Path

sender = "thoonthoon469@gmail.com"
apppassword = "vhhk jbnp qdao yvjo"

receiver = "thoonlay779@gmail.com"
subject = "Test Email from Python OOP"


# HTML Template
htmlbody = Template(Path("index.html").read_text())

gmail = GmailSender(sender,apppassword)
gmail.send(receiver,subject,htmlbody)