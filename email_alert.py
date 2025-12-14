import smtplib
from email.message import EmailMessage

EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

def send_email(file_path):
    msg = EmailMessage()
    msg["Subject"] = "SECURITY ALERT – FAILED LOGIN DETECTED"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    msg.set_content("Encrypted intruder image attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=file_path.split("\\")[-1]
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
