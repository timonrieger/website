import requests, os
from main import app, db, AirNomads

SHEETY_ALL_ENDPOINT = "https://api.sheety.co/e2e4da57cedbf59fa0d734324f84fc00/flightDeals"
TRAVEL_DATA = f"{os.environ.get("TRAVEL_DATA")}"
SHEETY_BEARER = os.environ.get("SHEETY_BEARER")

HEADER = {
    "Authorization": f"Bearer {SHEETY_BEARER}"
}

class DataManager:
    # This class is responsible for talking to the Google Sheet and the Database.

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}


    def get_user_data(self):
        with app.app_context():
            user_data = db.session.query(AirNomads).all()
        self.user_data = [{"token": user.token, "id": user.id, "username": user.username, "email": user.email,
                           "departureCity": user.departure_city, "departureIata": user.departure_iata,
                           "currency": user.currency, "nightsFrom": user.min_nights, "nightsTo": user.max_nights,
                           "dreamPlaces": user.travel_countries.split(",")} for user in user_data if user.confirmed == 1]
        return self.user_data

    def get_destination_data(self):
        self.destination_data = requests.get(url=TRAVEL_DATA).json()["countries"]
        return self.destination_data


########## test if sheety is usable ################

# response = requests.get(url=f"{SHEETY_ALL_ENDPOINT}/users", headers=HEADER)
# if response.status_code != 200:
#     print(response.text)
#     exit()
# else:
#     print(response.json())