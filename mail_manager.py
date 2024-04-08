import secrets, string, smtplib

class MailManagaer():

    def __init__(self):
        self.confirmation_token = ""


    def send_confirmation_link(self, to_email, email, email_password, form):
        """Send a confirmation link to the specified email."""
        # Generate a random token
        characters = string.ascii_letters + string.digits
        self.confirmation_token = ''.join(secrets.choice(characters) for i in range(20))
        confirmation_link = f"http://127.0.0.1:5000/confirm/{to_email}?token={self.confirmation_token}&form={form}"
        message = (f"Subject: Account Confirmation Link\n\n"
                   f"Hello,\n\n"
                   f"Thank you for signing up! To complete your registration, please click the link below:\n\n{confirmation_link}\n\n"
                   f"If you did not request this registration or have any questions, please ignore this message.\n\n"
                   f"Best regards,\n\nTimon Rieger")

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(email, email_password)
                server.sendmail(email, to_email, message)

    def check_token(self, token):
        return token == self.confirmation_token
