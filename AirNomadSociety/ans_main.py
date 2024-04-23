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
    dream_places = []
    gem_places = []

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
                dream_places.append(
                    {
                        "price": int(float(flight.price[0])),
                        "currency": flight.currency,
                        "dep_city": flight.departure_city[0],
                        "dep_code": flight.departure_iata_code[0],
                        "arr_city": flight.arrival_city[0],
                        "arr_code": flight.arrival_iata_code[0],
                        "arr_country": flight.arrival_country,
                        "from_dt": flight.from_date[0],
                        "to_dt": flight.to_date[0],
                        "link": flight.link,
                        "stop_over": flight.via_city
                    }
                )

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
            gem_places.append(
                {
                    "price": int(float(flight.price[0])),
                    "currency": flight.currency,
                    "dep_city": flight.departure_city[0],
                    "dep_code": flight.departure_iata_code[0],
                    "arr_city": flight.arrival_city[0],
                    "arr_code": flight.arrival_iata_code[0],
                    "arr_country": flight.arrival_country,
                    "from_dt": flight.from_date[0],
                    "to_dt": flight.to_date[0],
                    "link": flight.link,
                    "stop_over": flight.via_city
                }
            )

    notification_manager.send_weekly_email(to_address=user["email"], dream_flights=dream_places, random_flights=gem_places, username=user['username'])

    print(f"Code Run Time was: {time.time() - start_time} seconds.")

