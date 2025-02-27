import random

import pyperclip
from scripts import readwise_client
import openai

def get_all_highlights():
  return readwise_client.get(endpoint="/highlights/").json()

def select_random(res):
  return random.choice(res['results'])

def ask_ai(text):

  client = openai.OpenAI(api_key='APIKEY', base_url='http://127.0.0.1:1337/v1')

  response = client.chat.completions.create(
      model="qwen2.5-coder-7b-instruct",
      messages=[
        {"role": "system", "content": "You are a Quote Researcher"},
        {"role": "assistant", "content": "Find the author of the quote. Then output the quote and the author in the following format to stdout: 'quote' - author"},
        {"role": "user", "content": text}
      ],
    )

  response = response.choices[0].message.content
  return response


if __name__ == "__main__":
  highlights = [h['text'] for h in get_all_highlights()['results']]
  for highlight in highlights:
    print(ask_ai(highlight))

if __name__ == "hello":
  print("Fetching readwise highlights...")
  highlights = get_all_highlights()
  while True:
    highlight = select_random(highlights)
    highlight_content = highlight['text']
    print(f"\nChose highlight:\n\n{highlight_content}")
    pyperclip.copy(highlight_content)
    print("Copied highlight...")
    if input("Hit enter to select new highlight: \n") != "":
      break

