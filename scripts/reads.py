# /// script
# requires-python = ">3.10"
# dependencies = [
#   "requests>=2.32.5,<3.0.0",
# ]
# ///

import os
import requests
from datetime import datetime, timedelta

readwise_token = os.getenv("READWISE_KEY")
readwise_headers = {"Authorization": f"Token {readwise_token}"}
readwise_base_url = "https://readwise.io/api"

FILE = "content/reads.md"

DATE_FORMAT = "%b %d, %Y"

BOOKS = "books"
ARTICLES = "articles"
TWEETS = "tweets"
PODCASTS = "podcasts"


def get_readwise_data(category):
    response = requests.get(
        f"{readwise_base_url}/v2/books/",
        params={"category": category, "page_size": 1000, "page": 1},
        headers=readwise_headers,
    )
    response = response.json()["results"]
    item_list = [
        {
            "title": item["title"],
            "author": item["author"]
            .split(",")[0]
            .split(" and")[0]
            .split(" und")[0]
            .split(" &")[0],
            "date": (
                datetime.fromisoformat(item["last_highlight_at"])
                if item["last_highlight_at"]
                else datetime.fromisoformat(item["updated"])
            ),
            "highlights": item["num_highlights"],
            "url": (
                "https://amazon.com/dp/" + item["asin"]
                if category == BOOKS and item["asin"]
                else item["source_url"]
            ),
        }
        for item in response
        if item["title"] != "Quick Passages"
        and (item["num_highlights"] > 0 or category != BOOKS)
    ]
    last = sorted(item_list, key=lambda x: x["date"], reverse=True)[:10]
    favorites = (
        sorted(item_list, key=lambda x: x["highlights"], reverse=True)[:5]
        if category in [BOOKS, ARTICLES]
        else []
    )
    return {category: [favorites, last]}


def get_reader_data():
    # Get documents updated in last 30 days
    thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()
    item_list = []
    next_page_cursor = None
    while True:
        params = {"updatedAfter": thirty_days_ago}
        if next_page_cursor:
            params["pageCursor"] = next_page_cursor
        response = requests.get(
            f"{readwise_base_url}/v3/list/", params=params, headers=readwise_headers
        )
        res = response.json()
        try:
            data = res["results"]
        except KeyError:
            break
        item_list.extend(data)
        next_page_cursor = res.get("nextPageCursor")
        if not next_page_cursor:
            break
    item_list = [
        {
            "title": item["title"],
            "author": item["author"],
            "date": datetime.fromisoformat(item["created_at"]),
            "url": item["source_url"],
        }
        for item in item_list
        if item["reading_progress"] > 0  # Only include items that have been started
    ]
    return {"articles": [[], item_list[:10]]}


def gen_markdown(data):
    new_content = ""

    for category, lists in data.items():
        if lists[0]:
            new_content += f"\n\n## Favorite {category.capitalize()}\n\n"
            new_content += "\n".join(
                [
                    (
                        f"- [_{item['title']}_]({item['url']}) by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                        if item["url"]
                        else f"- _{item['title']}_ by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                    )
                    for item in lists[0]
                ]
            )
        if lists[1]:
            new_content += f"\n\n## Latest {category.capitalize()}\n\n"
            new_content += "\n".join(
                [
                    (
                        f"- [_{item['title']}_]({item['url']}) by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                        if item["url"]
                        else f"- _{item['title']}_ by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                    )
                    for item in lists[1]
                ]
            )

    return new_content


def update_file(file_path, new_content):
    # Get the current date and time for the lastmod field
    current_time = datetime.now().isoformat()

    with open(file_path, "r") as f:
        content = f.read()

    # Split into front matter, second --- and body
    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValueError("File does not have a valid structure with front matter.")

    # Front matter (first part) and body (third part)
    front_matter = parts[0] + "---" + parts[1] + "---"

    # Replace the lastmod field with the current time
    front_matter_lines = front_matter.splitlines()
    for i, line in enumerate(front_matter_lines):
        if line.startswith("lastmod:"):
            front_matter_lines[i] = f"lastmod: '{current_time}'"

    # Combine the updated front matter with the new content
    updated_content = f"{'\n'.join(front_matter_lines)}{new_content}"

    # Write back to the file
    with open(file_path, "w") as f:
        f.write(updated_content)
    print(f"Updated {file_path}")


if __name__ == "__main__":
    file_path = FILE
    book_dict = get_readwise_data(BOOKS)
    reader_dict = get_reader_data()
    reader_dict["articles"][0] = get_readwise_data(ARTICLES)[ARTICLES][
        0
    ]  # merge favorite articles from readwise with latest articles from reader
    data = book_dict | reader_dict
    new_content = gen_markdown(data)
    update_file(file_path, new_content)
