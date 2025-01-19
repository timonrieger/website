import dotenv
import os

dotenv.load_dotenv()

NPOINT = os.getenv("NPOINT")
CONTACT_EMAIL = os.getenv("CONTACT_EMAIL")
READWISE_KEY = os.getenv("READWISE_KEY")
SOCIALS = {
    "linkedin": "https://www.linkedin.com/in/timon-rieger",
    "github": "https://github.com/timonrieger",
    "twitter": "https://x.com/timonrieger",
    "email": f"mailto:{CONTACT_EMAIL}",
}
STATUS_PAGE = "https://stats.uptimerobot.com/nrF9tU3KtX"
BLOG_URL = "https://blog.timonrieger.de"
SECRET_KEY = os.getenv("SECRET_KEY")
