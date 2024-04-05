import smtplib
from email.message import EmailMessage


def send_mail(to_mail,Cust_name,message):
    # Outlook server and port
    smtp_server = "smtp-mail.outlook.com"
    port = 587

    # Get user input for recipient, message, and credentials
    # recipient = input("Enter recipient email: ")
    # message = input("Enter email message: ")
    sender_email = "anupam.coder@outlook.com"
    password = "@kolkata700032@"

    # Create email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = to_mail
    msg['Subject'] = (f"BANK DETAILS-{Cust_name}")
    msg.set_payload(message)

    # Connect and send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, password)
        server.send_message(msg)
        print("Details already sent to given mail id!")
