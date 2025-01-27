from scripts import readwise_client
from datetime import datetime

FILE = "content/reads.md"

DATE_FORMAT = "%b, %y"

BOOKS = "books"
ARTICLES = "articles"
TWEETS = "tweets"
PODCASTS = "podcasts"


def get_data(category):
    response = readwise_client.get_books(category=category)
    item_list = [
        {
            "title": item.title,
            "author": item.author.split(",")[0]
            .split(" and")[0]
            .split(" und")[0]
            .split(" &")[0],
            "date": item.last_highlight_at if item.last_highlight_at else item.updated,
            "highlights": item.num_highlights,
            "url": item.source_url,
        }
        for item in response
        if item.title != "Quick Passages"
        and (item.num_highlights > 1 or category != BOOKS)
    ]
    last_10 = sorted(item_list, key=lambda x: x["date"], reverse=True)[:10]
    most_highlighted = sorted(item_list, key=lambda x: x["highlights"], reverse=True)[
        :5
    ]
    return {category: [most_highlighted, last_10]}


def gen_markdown(data):
    new_content = ""

    for category, lists in data.items():
        new_content += f"\n\n## {category.capitalize()}"
        new_content += "\n\n### Most Highlighted\n\n"
        new_content += "\n".join(
            [
                f"- [_{item['title']}_]({item['url']}) by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                if item['url']
                else f"- _{item['title']}_ by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                for item in lists[0]
            ]
        )
        new_content += "\n\n### Latest Ten\n\n"
        new_content += "\n".join(
            [
                f"- [_{item['title']}_]({item['url']}) by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
                if item['url']
                else f"- _{item['title']}_ by {item['author']} ({item['date'].strftime(DATE_FORMAT)})"
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
    body = parts[2]

    # Replace the lastmod field with the current time
    front_matter_lines = front_matter.splitlines()
    for i, line in enumerate(front_matter_lines):
        if line.startswith("lastmod:"):
            front_matter_lines[i] = f"lastmod: '{current_time}'"

    # Combine the updated front matter with the new content
    updated_content = f"{"\n".join(front_matter_lines)}{new_content}"

    # Write back to the file
    with open(file_path, "w") as f:
        f.write(updated_content)
    print(f"Updated {file_path} with new lastmod and content.")


if __name__ == "__main__":
    file_path = FILE
    book_dict = get_data(BOOKS)
    article_dict = get_data(ARTICLES)
    data = book_dict | article_dict
    new_content = gen_markdown(data)
    update_file(file_path, new_content)
