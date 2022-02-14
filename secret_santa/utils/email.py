import smtplib
from email.mime.text import MIMEText

gmail_base = "LenaTheBot"
gmail_u = gmail_base + "@gmail.com"

sent_from = gmail_u
to = ['iurii.paustovskii@gmail.com', 'maxinmostlight@gmail.com', 'tkachencomaria@gmail.com']
# subject = 'Secret Santa'

gmail_p = gmail_base + "2021"


def send_email(subject, text):
    email_text = "\r\n".join([
        "From: %s",
        "To: %s",
        "Subject: %s",
        "",
        text])

    email_text = email_text % (sent_from, ", ".join(to), subject)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_u, gmail_p)
    server.sendmail(sent_from, to, email_text.encode("utf8"))
    server.close()
    print('Email sent!')