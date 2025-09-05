from gmailsender import GmailSender

sender = "thoonthoon469@gmail.com"
apppassword = "vhhk jbnp qdao yvjo"

receiver = "thoonlay779@gmail.com"
subject = "Test Email from Python OOP"
body = "This is a test email sent from Python class using Gmail SMTP."

gmail = GmailSender(sender,apppassword)
gmail.send(receiver,subject,body)