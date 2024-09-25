import secrets, string, smtplib, time, os
from PIL import Image, ExifTags
from fractions import Fraction

PHOTOS_DIR = 'static/images/photography'

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
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(my_mail, email_password)
                server.sendmail(my_mail, user_mail, message)
            return True
        except Exception:
            return False

    def check_expiring_token(self, token, valid_time):
        """Check if a token is valid within the specified time."""
        if token in self.tokens:
            creation_time = self.tokens[token]
            current_time = time.time()
            # Check if token was created within the valid time
            if current_time - creation_time <= valid_time:
                return True
            else:
                del self.tokens[token]
            return False
        return False


    def send_confirmation_email(self,user_mail, my_mail, email_password, form, db, NewsletterSubs, AirNomads, username=""):
        """Send a confirmation link to the specified email."""
        token = self.generate_token(expire=True)
        user_id = self.get_user_id(user_mail, form, db, NewsletterSubs, AirNomads)
        confirmation_link = f"https://www.timonrieger.de/confirm?id={user_id}&token={token}&form={form}"
        message = (f"Subject: Account Confirmation Link\n\n"
                   f"Hello {username},\n\n"
                   f"Thank you for signing up! To complete your registration, please click the link below within the next 10 minutes:\n\n"
                   f"{confirmation_link}\n\n"
                   f"If you did not request this registration or have any questions, please ignore this message.\n\n"
                   f"Best regards,\n\nTimon Rieger")
        return self.send_basic_emails(my_mail, email_password, user_mail, message)


def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is not None:
        exif = {
            ExifTags.TAGS.get(tag): value
            for tag, value in exif_data.items()
            if tag in ExifTags.TAGS
        }
        return exif
    else:
        return None

def get_exposure_info(exif):
    aperture = exif.get("FNumber")
    shutter_speed = exif.get("ExposureTime")
    iso = exif.get("ISOSpeedRatings")
    if aperture and shutter_speed and iso:
        aperture_value = aperture.numerator / aperture.denominator
        shutter_speed_value = Fraction(shutter_speed).limit_denominator()
        exposure_info = f" | f{aperture_value} | {shutter_speed_value}s | ISO {iso}"
        return exposure_info
    return ""

def get_camera_info(exif):
    lens = exif.get("LensModel")
    model = exif.get("Model", "").strip()
    lens_mm = round(exif.get("FocalLength"), 0)
    if model and lens:
        return f" | {lens} | {model} | {lens_mm}mm"
    return ""

def build_photo_list():
    all_photos = []
    for filename in os.listdir(PHOTOS_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(PHOTOS_DIR, filename)
            exif = get_exif_data(image_path)
            exposure_info = get_exposure_info(exif) if exif else None
            camera_info = get_camera_info(exif) if exif else None
            photo_info = {
                "filename": filename,
                "camera": camera_info,
                "exposure": exposure_info,
                "date": exif['DateTimeOriginal']
            }
            all_photos.append(photo_info)
    return all_photos

