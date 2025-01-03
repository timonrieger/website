import dotenv
import os

dotenv.load_dotenv()

NPOINT = os.getenv("NPOINT")
CONTACT_EMAIL = os.getenv("CONTACT_EMAIL")
READWISE_KEY = os.getenv("READWISE_KEY")
SOCIALS = {
    "linkedin": "https://www.linkedin.com/in/timon-rieger",
    "github": "https://github.com/timonrieger",
    "instagram": "https://instagram.com/timon_rgx",
    "twitter": "https://x.com/timonrieger",
    "email": f"mailto:{CONTACT_EMAIL}"
}
