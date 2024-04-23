import secrets, string, smtplib, time

class MailManager():

    def __init__(self):
        self.tokens = {}

    def generate_token(self, expire):
        characters = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(characters) for i in range(20))
        if expire:
            self.tokens[token] = time.time()
        return token

    def get_user_id(self, user_mail, form, db, NewsletterSubs, AirNomads):
        if form == "newsletter":
            member = db.session.execute(db.Select(NewsletterSubs).where(NewsletterSubs.email == user_mail)).scalar()
        elif form == "ans":
            member = db.session.execute(db.Select(AirNomads).where(AirNomads.email == user_mail)).scalar()
        user_id = member.id
        return user_id

    def send_basic_emails(self, my_mail, email_password, user_mail, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(my_mail, email_password)
                server.sendmail(my_mail, user_mail, message)

    def check_expiring_token(self, token, valid_time):
        """Check if a token is valid within the specified time."""
        if token in self.tokens:
            creation_time = self.tokens[token]
            current_time = time.time()
            # Check if token was created within the valid time
            if current_time - creation_time <= valid_time:
                return True
            else:
                del self.tokens[token]  # Remove expired token
            return False
        return False  # Token does not exist


    def send_confirmation_email(self, user_mail, my_mail, email_password, form, db, NewsletterSubs, AirNomads):
        """Send a confirmation link to the specified email."""
        token = self.generate_token(expire=True)
        user_id = self.get_user_id(user_mail, form, db, NewsletterSubs, AirNomads)
        confirmation_link = f"http://127.0.0.1:5000/confirm?id={user_id}&token={token}&form={form}"
        message = (f"Subject: Account Confirmation Link\n\n"
                   f"Hello,\n\n"
                   f"Thank you for signing up! To complete your registration, please click the link below within the next 10 minutes:\n\n"
                   f"{confirmation_link}\n"
                   f"If you did not request this registration or have any questions, please ignore this message.\n\n"
                   f"Best regards,\n\nTimon Rieger")
        self.send_basic_emails(my_mail, email_password, user_mail, message)
