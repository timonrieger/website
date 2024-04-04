from datetime import datetime, timedelta
import random, time

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# reloading_requests = 0
start_time = time.time()

data_manager.get_user_data()

data_manager.get_destination_data()

for user in data_manager.user_data:
    selected_gems = random.sample(data_manager.destination_data, 5)
    for index, item in enumerate(selected_gems):
        while item in user["dreamPlaces"]:
            selected_gems[index] = random.choice(data_manager.destination_data)
            item = selected_gems[index]
    message = f"Hey {user["username"]}!\n\n"
    dream_places = "🌟 Your Favorite Destinations 🌟\n\n"
    gem_places = "💎 Discover Hidden Gems 💎\n\n"

    for destination in data_manager.destination_data:
        # reloading_requests += 1
        if destination["country"] == "" or destination["code"] == "":
            pass  # in case there is an empty line, skip this destination

        if destination["country"] in user["dreamPlaces"]:
            flight = flight_search.check_flight(
                departure_iata_code=user["departureIata"],
                arrival_iata_code=destination["code"],
                from_time=datetime.now() + timedelta(days=1),
                to_time=datetime.now() + timedelta(days=180),
                min_nights=user["nightsFrom"],
                max_nights=user["nightsTo"],
                currency=user["currency"].upper()
            )
            if flight is None:
                continue

            elif flight.departure_city[0] != flight.arrival_city[0]:
                dream_places += (
                    f"✈️ Only {flight.price[0]}{flight.currency} to fly from "
                    f"{flight.departure_city[0]} ({flight.departure_iata_code[0]}) to "
                    f"{flight.arrival_city[0]} ({flight.arrival_iata_code[0]}), {flight.arrival_country}, "
                    f"from {flight.from_date[0]} to {flight.to_date[0]}.")
                if flight.stop_overs[0] > 0:
                    dream_places += f" Flight has {flight.stop_overs[0]} stop over in {flight.via_city}."
                dream_places += "\n\n"

    for destination in selected_gems:
        flight = flight_search.check_flight(
            departure_iata_code=user["departureIata"],
            arrival_iata_code=destination["code"],
            from_time=datetime.now() + timedelta(days=1),
            to_time=datetime.now() + timedelta(days=180),
            min_nights=user["nightsFrom"],
            max_nights=user["nightsTo"],
            currency=user["currency"].upper()
        )
        if flight is None:
            continue

        elif flight.departure_city[0] != flight.arrival_city[0]:
            gem_places += (
                f"✈️ Only {flight.price[0]}{flight.currency} to fly from "
                f"{flight.departure_city[0]} ({flight.departure_iata_code[0]}) to "
                f"{flight.arrival_city[0]} ({flight.arrival_iata_code[0]}), {flight.arrival_country}, "
                f"from {flight.from_date[0]} to {flight.to_date[0]}.")
            if flight.stop_overs[0] > 0:
                gem_places += f" Flight has {flight.stop_overs[0]} stop over in {flight.via_city}."
            gem_places += "\n\n"

    message += f"{dream_places}\n\n\n{gem_places}\n\n\nHappy Travels!"
    notification_manager.send_emails(to_adress=user["email"], message=message)

    print(f"Code Run Time was: {time.time() - start_time} seconds.")

