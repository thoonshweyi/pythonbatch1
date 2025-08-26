from gmailsender import GmailSender

sender = "datalandtechnology@gmail.com"
apppassword = ""

receiver = "tinhtutaung.dlt@gmail.com"
subject = "Test Email from Python OOP"
body = "This is a test email sent from Python class using Gmail SMTP."

gmail = GmailSender(sender,apppassword)
gmail.send(receiver,subject,body)