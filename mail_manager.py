import secrets, string, smtplib

class MailManagaer():

    def __init__(self):
        self.tokens = {}


    def send_confirmation_link(self, to_email, email, email_password, form):
        """Send a confirmation link to the specified email."""
        # Generate a random token
        characters = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(characters) for i in range(20))
        self.tokens[token] = time.time()
        # get user id
        if form == "newsletter":
            member = db.session.execute(db.Select(NewsletterSubs).where(NewsletterSubs.email == user_mail)).scalar()
        elif form == "ans":
            member = db.session.execute(db.Select(AirNomads).where(AirNomads.email == user_mail)).scalar()
        user_id = member.id
        # create the link
        confirmation_link = f"http://127.0.0.1:5000/confirm?id={user_id}&token={token}&form={form}"
        #write the email
        message = (f"Subject: Account Confirmation Link\n\n"
                   f"Hello,\n\n"
                   f"Thank you for signing up! To complete your registration, please click the link below:\n\n{confirmation_link}\n"
                   f"This link will remain valid for 10 minutes.\n\n"
                   f"If you did not request this registration or have any questions, please ignore this message.\n\n"
                   f"Best regards,\n\nTimon Rieger")

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(email, email_password)
                server.sendmail(email, to_email, message)

    def check_token(self, token):
        print(self.tokens)
        print(time.time())
        if token in self.tokens:
            creation_time = self.tokens[token]
            current_time = time.time()
            # Check if token was created within the last ten minutes
            if current_time - creation_time <= 600:
                return True
            else:
                del self.tokens[token]  # Remove expired token
        return False
