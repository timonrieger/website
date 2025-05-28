import dotenv
import os

dotenv.load_dotenv()
readwise_token = os.getenv("READWISE_KEY")
readwise_headers = {
    'Authorization': f'Token {readwise_token}'
}
readwise_base_url = 'https://readwise.io/api'
