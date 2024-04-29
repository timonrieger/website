from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from forms import AirNomadSocietyForm, NewsletterForm, ContactForm, FlashbackPlaylistsForm
import requests, os
from flask_bootstrap import Bootstrap5
from FlashbackPlaylists.spotify import PlaylistGenerator
from mail_manager import MailManager
from flask_wtf.csrf import CSRFProtect

# website content storage using npoint
npoint_data = requests.get(url="https://api.npoint.io/498c13e5c27e87434a9f").json()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

csrf = CSRFProtect()
csrf.init_app(app)

GMAIL_EMAIL = os.environ.get("GMAIL_EMAIL")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")
ANS_EMAIL = os.environ.get("ANS_EMAIL")
ANS_MAIL_PASSWORD = os.environ.get("ANS_MAIL_PASSWORD")


bootstrap = Bootstrap5(app)

mail_manager = MailManager()

class Base(DeclarativeBase):
    __abstract__ = True

    confirmed: Mapped[int] = mapped_column(Integer, default=0)
    token: Mapped[str] = mapped_column(String, unique=True)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///portfolio-website.db"
db = SQLAlchemy(app, model_class=Base)

class AirNomads(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    departure_city: Mapped[str] = mapped_column(String)
    departure_iata: Mapped[str] = mapped_column(String)
    currency: Mapped[str] = mapped_column(String)
    min_nights: Mapped[int] = mapped_column(Integer)
    max_nights: Mapped[int] = mapped_column(Integer)
    travel_countries: Mapped[str] = mapped_column(String)

class NewsletterSubs(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String, unique=True)

with app.app_context():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def home():
    form = NewsletterForm()
    if form.validate_on_submit():
        already_subscriber = db.session.execute(db.Select(NewsletterSubs).where(NewsletterSubs.email == form.email.data)).scalar()
        if already_subscriber:
            flash("You are already subscribed.")
        else:
            newsletter_subscriber = NewsletterSubs(email=form.email.data, token=mail_manager.generate_token(expire=False))
            db.session.add(newsletter_subscriber)
            db.session.commit()
            mail_manager.send_confirmation_email(form.email.data, GMAIL_EMAIL, GMAIL_PASSWORD, "newsletter", db, NewsletterSubs, AirNomads)
            flash(f"Confirmation email sent to {form.email.data}. Check your inbox and click the link.")

    return render_template("index.html", form=form)

@app.route("/confirm")
def confirm_users():
    token = request.args.get("token")
    form = request.args.get("form")
    id = request.args.get("id")
    if form == "newsletter":
        member = db.session.execute(db.Select(NewsletterSubs).where(NewsletterSubs.id == id)).scalar()
        if member and member.confirmed == 1:
            flash("You have already confirmed your subscription. Stay tuned!")
        elif mail_manager.check_expiring_token(token, 600):
            member.confirmed = 1
            flash("Successfully subscribed.")
        else:
            db.session.delete(member)
            flash("Invalid confirmation token. Please fill in the form again.")
        db.session.commit()
        return redirect(url_for("home"))

    elif form == "ans":
        member = db.session.execute(db.Select(AirNomads).where(AirNomads.id == id)).scalar()
        if member and member.confirmed == 1:
            flash("You have already confirmed your subscription. Sit back and relax!")
            return redirect(url_for("air_nomad_society", id=id))
        elif mail_manager.check_expiring_token(token, 600):
            member.confirmed = 1
            db.session.commit()
            flash("Success! You are now an Air Nomad ✈️. Feel free to update your profile as needed.")
            return redirect(url_for("air_nomad_society", id=id))
        else:
            flash("Invalid confirmation token. Please resubmit the form and click the link in the email within 10 minutes.")
            return redirect(url_for("air_nomad_society", id=id, unsubscribe=True))


@app.route("/unsubscribe")
def unsubscribe_users():
    token = request.args.get("token")
    form = request.args.get("form")
    if form == "newsletter":
        member = db.session.execute(db.Select(NewsletterSubs).where(NewsletterSubs.token == token)).scalar()
        db.session.delete(member)
        db.session.commit()
        flash(f"Successfully unsubscribed with {member.email}.")
        return redirect(url_for("home"))

    elif form == "ans":
        member = db.session.execute(db.Select(AirNomads).where(AirNomads.token == token)).scalar()
        if member:
            flash(f"Successfully unsubscribed with {member.email}. To resubscribe, simply fill out the form again.")
            return redirect(url_for("air_nomad_society", token=token, unsubscribe=True))
        if not member:
            flash("You are already unsubscribed.")
            return redirect(url_for("air_nomad_society"))



@app.route("/air-nomad-society", methods=["POST", "GET"])
def air_nomad_society():
    token = request.args.get("token")
    id = request.args.get("id")
    form = AirNomadSocietyForm()
    # update user profile or delete user
    if token or id:
        unsubscribe = request.args.get("unsubscribe")
        if token:
            member = db.session.execute(db.Select(AirNomads).where(AirNomads.token == token)).scalar()
        elif id:
            member = db.session.execute(db.Select(AirNomads).where(AirNomads.id == id)).scalar()
        else:
            member = None

        if not member and not unsubscribe:
            flash("You are not a member anymore. Subscribe again to update your profile.")
        elif member:
            form = AirNomadSocietyForm(
                username=member.username,
                email=member.email,
                departure_city=f"{member.departure_city} | {member.departure_iata}",
                currency=member.currency,
                min_nights=member.min_nights,
                max_nights=member.max_nights,
                favorite_countries=[country.replace(",", "") for country in member.travel_countries.split(",")]
            )
            if unsubscribe:
                db.session.delete(member)
                db.session.commit()

    if form.validate_on_submit():
        already_member = db.session.execute(db.Select(AirNomads).where(AirNomads.email == form.email.data)).scalar()
        favorite_countries = ",".join([country for country in form.favorite_countries.data])
        if already_member:
            if form.update.data:
                already_member.username = form.username.data
                already_member.departure_city = form.departure_city.data.split(" | ")[0]
                already_member.departure_iata = form.departure_city.data.split(" | ")[1]
                already_member.currency = form.currency.data
                already_member.min_nights = form.min_nights.data
                already_member.max_nights = form.max_nights.data
                already_member.travel_countries = favorite_countries
                db.session.commit()
                flash("Your preferences were changed successfully.")
            elif form.join.data:
                flash("You are already a member. Update instead.")
        if not already_member:
            if form.update.data:
                flash("You aren't a member yet. Join first.")
            elif form.join.data:
                new_member = AirNomads(
                    username=form.username.data,
                    email=form.email.data,
                    departure_city=form.departure_city.data.split(" | ")[0],
                    departure_iata=form.departure_city.data.split(" | ")[1],
                    currency=form.currency.data,
                    min_nights=form.min_nights.data,
                    max_nights=form.max_nights.data,
                    travel_countries=favorite_countries,
                    token=mail_manager.generate_token(expire=False)
                )
                db.session.add(new_member)
                db.session.commit()
                mail_manager.send_confirmation_email(form.email.data, ANS_EMAIL, ANS_MAIL_PASSWORD, "ans", db, NewsletterSubs, AirNomads, username=form.username.data)
                flash(f"Confirmation email sent to {form.email.data}. Check your inbox and click the link.")


    return render_template("AirNomad.html", form=form)

@app.route("/flashback-playlists", methods=["POST", "GET"])
def flashback_playlists():
    form = FlashbackPlaylistsForm()
    if form.validate_on_submit():
        date_input = str(form.date_input.data)
        year = int(date_input.split("-")[0])
        month = date_input.split("-")[1]
        day = date_input.split("-")[2]
        if year >= 1900:
            playlist_date = f"{year}-{month}-{day}"
            description = f"{form.description.data}\nCreated by https://www.example.com"
            playlist_link = PlaylistGenerator.generate_playlist(date=playlist_date, title=form.title.data, description=description)
            return render_template("FlashbackPlaylists.html", form_submitted=True, link=playlist_link, title=form.title.data, form=form)
        else:
            flash("Please enter a date that is later than 1900.")
            form = FlashbackPlaylistsForm(
                title=form.title.data,
                description=form.description.data
            )
            return render_template("FlashbackPlaylists.html", form=form)
    return render_template("FlashbackPlaylists.html", form=form)


@app.route("/projects")
def browse_projects():
    return render_template("projects.html", all_projects=npoint_data["projects"])

@app.route("/contact", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return render_template("contact.html", form=form, form_submitted=True)
    return render_template("contact.html", form=form)

if __name__ == "__main__":
    app.run(debug=False)