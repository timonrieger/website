import random

import pyperclip
from scripts import readwise_client

def get_all_highlights():
  return readwise_client.get(endpoint="/highlights/").json()

def select_random(res):
  return random.choice(res['results'])

if __name__ == "__main__":
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

