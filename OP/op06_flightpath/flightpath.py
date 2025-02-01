"""Flightpath."""


def update_delayed_flight(schedule: dict[str, tuple[str, str]], delayed_flight_number: str, new_departure_time: str) -> \
        dict[str, tuple[str, str]]:
    """
    Update the departure time of a delayed flight in the flight schedule.

    Return a dictionary where the departure time of the specified flight is modified.
    This means that the result dictionary should not contain the old time,
    instead a new departure time points to the specified flight.
    The input schedule cannot be changed.

    :param schedule: Dictionary of flights ({time string: (destination, flight number)})
    :param delayed_flight_number: Flight number of the delayed flight
    :param new_departure_time: New departure time for the delayed flight
    :return: Updated flight schedule with the delayed flight's departure time changed
    """
    updated_schedule = {}
    for departure_time, flight_info in schedule.items():
        if delayed_flight_number in flight_info:
            departure_time = new_departure_time
        if departure_time not in updated_schedule:
            updated_schedule[departure_time] = flight_info
    return updated_schedule


def cancel_flight(schedule: dict[str, tuple[str, str]], cancelled_flight_number: str) -> dict[str, tuple[str, str]]:
    """
    Create a new schedule where the specified flight is cancelled.

    The function cannot modify the existing schedule parameter.
    Instead, create a new dictionary where the cancelled flight is not added.

    :param schedule: Dictionary of flights ({time: (destination, flight number)})
    :param cancelled_flight_number: Flight number of the cancelled flight
    :return: New flight schedule with the cancelled flight removed
    """
    updated_schedule = {}
    for departure_time, flight_info in schedule.items():
        if cancelled_flight_number in flight_info:
            continue
        elif departure_time not in updated_schedule:
            updated_schedule[departure_time] = flight_info
    return updated_schedule


def busiest_time(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour(s) at the airport based on the flight schedule.

    The busiest hour(s) is/are determined by counting the number of flights departing in each hour of the day.
    All flights departing with the same hour in their departure time, are counted into the same hour.

    The function returns a list of strings of the busiest hours, sorted in ascending order, such as ["08", "21"].

    :param schedule: Dictionary containing the flight schedule, where keys are departure times
                     in the format "HH:mm" and values are tuples containing destination and flight number.
    :return: List of strings representing the busiest hour(s) in 24-hour format, such as ["08", "21"].
    """
    hour_count = {}
    busiest_hours = []
    for departure_time in schedule.keys():
        hour = departure_time[:2]
        hour_count[hour] = hour_count.get(hour, 0) + 1

    max_flights = max(hour_count.values())
    for hour, count in hour_count.items():
        if count == max_flights:
            busiest_hours.append(hour)
    return busiest_hours


def connecting_flights(schedule: dict[str, tuple[str, str]], arrival: tuple[str, str]) -> list[tuple[str, str]]:
    """
    Find connecting flights based on the provided arrival information and flight schedule.

    The function takes a flight schedule and the arrival time and location of a flight,
    and returns a list of available connecting flights. A connecting flight is considered
    available if its departure time is at least 45 minutes after the arrival time, but less
    than 4 hours after the arrival time. Additionally, a connecting flight must not go back
    to the same place the arriving flight came from.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :param arrival: Tuple containing the arrival time and the location the flight is
                    arriving from. For example:
                    ("11:05", "Tallinn")

    :return: A list of tuples containing the departure time and destination of the
             available connecting flights, sorted by departure time. For example:
             [
                 ("14:00", "Paris"),
                 ("15:00", "Berlin")
             ]
             If no connecting flights are available, the function returns an empty list.
    """
    arrival_time, arrival_location = arrival
    arrival_hour, arrival_minute = map(int, arrival_time.split(':'))
    arrival_time_minutes = arrival_hour * 60 + arrival_minute

    min_departure_time = arrival_time_minutes + 45  #if its departure time is at least 45 minutes after the arrival time
    max_departure_time = arrival_time_minutes + 240  #but less than 4 hours after the arrival time

    available_flights = []

    for departure_time, (destination, flight_number) in schedule.items():
        departure_hour, departure_minute = map(int, departure_time.split(':'))
        departure_time_minutes = departure_hour * 60 + departure_minute

        if min_departure_time <= departure_time_minutes < max_departure_time and destination != arrival_location:
            # без destination != arrival_location -> ('06:15', 'Tallinn') а в арривал у тебя тоже Таллинн лол
            available_flights.append((departure_time, destination))

    return sorted(available_flights)


def busiest_hour(schedule: dict[str, tuple[str, str]]) -> list[str]:
    """
    Find the busiest hour-long slot(s) in the schedule.

    One hour slot duration is 60 minutes (or the diff of two times is less than 60).
    So, 15:00 and 16:00 are not in the same slot.

    :param schedule: Dictionary containing the flight schedule, where keys are departure
                     times in the format "HH:mm" and values are tuples containing
                     destination and flight number. For example:
                     {
                         "14:00": ("Paris", "FL123"),
                         "15:00": ("Berlin", "FL456")
                     }

    :return: A list of strings representing the starting time(s) of the busiest hour-long
             slot(s) in ascending order. For example:
             ["08:00", "15:20"]
             If the schedule is empty, returns an empty list.
    """
    #print(busiest_hour(flight_schedule))
    # ['06:15', '06:30', '07:29', '11:30']
    # 19:35 does not match because 20:35 is not in the same slot

    flight_schedule = {
        "04:35": ("Maardu", "MWL6754"),
        "06:15": ("Tallinn", "OWL6754"),
        "06:30": ("Paris", "OWL6751"),
        "07:29": ("London", "OWL6756"),
        "08:00": ("New York", "OWL6759"),
        "11:30": ("Tokyo", "OWL6752"),
        "11:35": ("Helsinki", "BHM2345"),
        "19:35": ("Paris", "BHM2346"),
        "20:35": ("Helsinki", "BHM2347"),
        "22:35": ("Tallinn", "TLN1001"),
    }

    hour_count = {}
    for departure_time in schedule.keys():
        hour = departure_time[:2]
        hour_count[hour] = hour_count.get(hour, 0) + 1
    #  print("hour cunt", hour_count)
    if not hour_count:
        return []

    max_count = max(hour_count.values())
    max_flights = [hour for hour in hour_count if hour_count[hour] == max_count]
    #  print("max flight", max_flights)


    busiest_hours = []
    for departure_time in schedule.keys():
        #print("D", departure_time)
        if departure_time[:2] in max_flights:
            #print(departure_time)
            hour_check = departure_time
            busiest_hours.append(departure_time)
        else:
            for busy_hour in max_flights:
                if departure_time[:2] == "{:02}".format(int(busy_hour) + 1):
                    print("Next hour found for busy hour:", departure_time)
                    busiest_hours.append(departure_time)
                    break  # Exit the loop after finding the next hour

    return busiest_hours


def most_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the most passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the most popular destination.
    """
    destination_count = {}
    for flight_info in schedule.values():
        destination, flight_number = flight_info
        if flight_number in passenger_count:
            destination_count[destination] = destination_count.get(destination, 0) + passenger_count[flight_number]

    return max(destination_count, key=destination_count.get)


def least_popular_destination(schedule: dict[str, tuple[str, str]], passenger_count: dict[str, int]) -> str:
    """
    Find the destination where the fewest passengers are going.

    :param schedule: A dictionary representing the flight schedule.
                     The keys are departure times and the values are tuples
                     containing destination and flight number.
    :param passenger_count: A dictionary with flight numbers as keys and
                            the number of passengers as values.
    :return: A string representing the least popular destination.
    """
    destination_count = {}
    for flight_info in schedule.values():
        destination, flight_number = flight_info
        if flight_number in passenger_count:
            destination_count[destination] = destination_count.get(destination, 0) + passenger_count[flight_number]
    # print(destination_count)
    return min(destination_count.keys(), key=destination_count.get)  # все таки уточни


if __name__ == '__main__':
    flight_schedule = {
        "06:15": ("Tallinn", "OWL6754"),
        "11:35": ("Helsinki", "BHM2345")
    }
    new_flight_schedule = update_delayed_flight(flight_schedule, "OWL6754", "09:00")
    print(flight_schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_flight_schedule)
    # {'09:00': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}

    new_flight_schedule = cancel_flight(flight_schedule, "OWL6754")
    print(flight_schedule)
    # {'06:15': ('Tallinn', 'OWL6754'), '11:35': ('Helsinki', 'BHM2345')}
    print(new_flight_schedule)
    # {'11:35': ('Helsinki', 'BHM2345')}

    flight_schedule = {
        "04:35": ("Maardu", "MWL6754"),
        "06:15": ("Tallinn", "OWL6754"),
        "06:30": ("Paris", "OWL6751"),
        "07:29": ("London", "OWL6756"),
        "08:00": ("New York", "OWL6759"),
        "11:30": ("Tokyo", "OWL6752"),
        "11:35": ("Helsinki", "BHM2345"),
        "19:35": ("Paris", "BHM2346"),
        "20:35": ("Helsinki", "BHM2347"),
        "22:35": ("Tallinn", "TLN1001"),
    }
    print(busiest_time(flight_schedule))
    # ['06', '11']

    print(connecting_flights(flight_schedule, ("04:00", "Tallinn")))
    # [('06:30', 'Paris'), ('07:29', 'London')]

    print(busiest_hour(flight_schedule))
    # ['06:15', '06:30', '07:29', '11:30']
    # 19:35 does not match because 20:35 is not in the same slot

    # flight number: number of passengers
    passenger_counts = {
        "MWL6754": 100,
        "OWL6754": 85,
        "OWL6751": 103,
        "OWL6756": 87,
        "OWL6759": 118,
        "OWL6752": 90,
        "BHM2345": 111,
        "BHM2346": 102,
        "BHM2347": 94,
        "TLN1001": 1
    }
    print(most_popular_destination(flight_schedule, passenger_counts))
    # Paris

    print(least_popular_destination(flight_schedule, passenger_counts))
    # Tallinn