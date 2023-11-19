from email.message import EmailMessage
import ssl
import smtplib
import Report_data
import os
import GUI

def send_mail(destination):
    ctx = ssl.create_default_context()
    attachment_paths = ["/path/to/file.xlsx", f"/path/to/{Report_data.Final_Topic_name}.docx"]
    for attachment_path in attachment_paths:
        if os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as file:
                file_data = file.read()
                em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=os.path.basename(attachment_path))
    with smtplib.SMTP_SSL(server, 465, context=ctx) as smtp:
        smtp.login(sender, passwrd)
        smtp.sendmail(sender, destination, em.as_string())
    sent = True
    return sent
sent = False
Completion_Status = {1: 'Completed', 0: 'Incomplete'}
Report_Status = Completion_Status[GUI.Status.get()]

server = "smtp.gmail.com"
sender = "pranaysinghorigami@gmail.com"
destination = ["pranaysinghorigami@gmail.com"]
passwrd = GUI.password.get()
name = "Pranay Kumar Singh"
Subject = f"{Report_data.Date}/ {name}/ Daily Report"
Content = f"Topic: {Report_data.Final_Topic_name}\nWord Count: {Report_data.Final_Word_count}\nStatus: {Completion_Status[False]}"

em = EmailMessage()
em['From'] = sender
em['To'] = ', '.join(destination)
em['Subject'] = Subject
em.set_content(Content)

if GUI.DAILY_BTN_PRESSED() and not sent:
    send_mail(destination)
    exit()