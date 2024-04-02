import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

sender_email = "subrata@XXXX.sg"
receiver_email_to = ["subrata_@XXXX.sg"]
receiver_email_cc = ["subrata.chatterjee@XXXX.com", "XXXX@XXXX.com","XX.XX@XX.com"]
def sendEmail(sender_email, receiver_email_to, receiver_email_cc, subject, body, attachment_path):
    # SMTP server configuration
    smtp_server = "XXXXXXXX"
    smtp_port = 25  # Change the port according to your SMTP server's configuration
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_email_to)
    msg['Cc'] = ", ".join(receiver_email_cc)
    msg['Subject'] = subject

    all_recipients = receiver_email_to + receiver_email_cc
    # Attach body to the email
    msg.attach(MIMEText(body, 'plain'))
    if attachment_path is not None and attachment_path != "":
    # Attach Excel file
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())        
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path}",
        )
        msg.attach(part)
        # Start SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Secure the connection
        #server.starttls()
        # Login to the SMTP server
        #server.login(smtp_username, smtp_password)
        # Send email
        server.sendmail(sender_email, all_recipients, msg.as_string())

    print("Email sent successfully.")
