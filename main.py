import json
from flask import Flask, render_template, redirect, request, send_from_directory
from flask_caching import Cache
import requests
from flask_bootstrap import Bootstrap5
import utils
from readwise import Readwise
from constants import BLOG_URL, READWISE_KEY, NPOINT, SECRET_KEY, SOCIALS, STATUS_PAGE

# website content storage using npoint
try:
    page_data = requests.get(url=NPOINT).json()
except Exception:
    with open("static/assets/content/backup-latest.json", "r") as file:
        page_data = json.load(file)

app = Flask(__name__)
app.secret_key = SECRET_KEY

cache = Cache(config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 600})
cache.init_app(app)

bootstrap = Bootstrap5(app)


@app.route("/", methods=["POST", "GET"])
def me():
    all_photos = sorted(utils.build_photo_list(), key=lambda x: x["date"], reverse=True)

    return render_template(
        "me.html", all_interests=page_data["interests"], photo_gallery=all_photos
    )


@app.route("/projects")
def projects():
    return render_template("projects.html", all_projects=page_data["projects"])


@app.route("/photography")
def photography():
    all_photos = sorted(utils.build_photo_list(), key=lambda x: x["date"], reverse=True)
    return render_template("photography.html", all_photos=all_photos)


@app.route("/books")
def books():
    client = Readwise(READWISE_KEY)
    books = client.get_books(category="books")
    book_list = [
        {
            "title": book.title,
            "author": book.author.split(",")[0]
            .split(" and")[0]
            .split(" und")[0]
            .split(" &")[0],
            "date": book.last_highlight_at if book.last_highlight_at else book.updated,
            "highlights": book.num_highlights,
        }
        for book in books
        if book.title != "Quick Passages" and book.num_highlights > 1
    ]
    latest_reads = sorted(book_list, key=lambda x: x["date"], reverse=True)[:5]
    best_reads = sorted(book_list, key=lambda x: x["highlights"], reverse=True)[:5]

    return render_template("books.html", latest=latest_reads, best=best_reads)


@app.route("/contact/<social>")
def contact(social):
    return redirect(SOCIALS[social])


@app.route("/status")
def status():
    return redirect(STATUS_PAGE)


@app.route("/blog")
def blog():
    return redirect(BLOG_URL)


@app.route("/robots.txt")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.after_request
def add_header(response):
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains; preload"
    )
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Cache-Control"] = "max-age=86400"
    return response


if __name__ == "__main__":
    app.run(debug=False)
