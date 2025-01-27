from readwise import Readwise
import dotenv
import os

dotenv.load_dotenv()
token = os.getenv("READWISE_KEY")
readwise_client = Readwise(token=token)
