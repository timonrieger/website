import dotenv
import os

dotenv.load_dotenv()

NPOINT_ANS = os.getenv("NPOINT_ANS")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")
ANS_EMAIL = os.getenv("ANS_EMAIL")
ANS_MAIL_PASSWORD = os.getenv("ANS_MAIL_PASSWORD")
PRV_EMAIL = os.getenv("PRV_EMAIL")
READWISE_KEY = os.getenv("READWISE_KEY")
NPOINT_ME=os.getenv("NPOINT_ME")
NPOINT_ANS = os.getenv("NPOINT_ANS")
DB_URI = os.getenv("DB_URI", "sqlite:///personal-website.db")
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")
ANS_EMAIL = os.getenv("ANS_EMAIL")
ANS_MAIL_PASSWORD = os.getenv("ANS_MAIL_PASSWORD")