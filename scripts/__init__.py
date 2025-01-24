from readwise import Readwise
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv("READWISE_KEY")
client = Readwise(token=token)
