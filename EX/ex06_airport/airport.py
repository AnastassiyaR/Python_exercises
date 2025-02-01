"""Airport schedule."""


def destinations_and_times(flights: list) -> dict:
    """
    Create a dictionary containing destinations with the departure times for this destination today.

    Flights in the list are in the format: "Tallinn,08:00,01h30m,OWL1234"
    Where different parts are separated by comma:
    - destination
    - departure time
    - flight duration
    - flight number

    Result format: {destination1: [time1, time2, ...], destination2: [time1, time2, ...]}.

    The order of departure times and destinations are not important.

    :param flights: given list from database.
    :return: dictionary where keys are destinations and values are lists of departure times.
    """
    a = {}

    for i in flights:
        if i.split(",")[0] not in a:
            a[i.split(",")[0]] = []
        a[i.split(",")[0]].append(i.split(",")[1])

    return a


def sort_dict_values(dictionary: dict) -> dict:
    """
    Sort dictionary values in ascending order.

    This function should be applied to the previous function's result to get the departure times ordered.

    Return a dictionary where all the values are in ascending order.
    The order of the keys is not important.
    """
    a = {}

    for x, i in dictionary.items():
        if x not in a:
            a[x] = []
        for j in i:
            a[x].append(j)
            a[x].sort()

    return a


def flights_to_destination(flights: list, destination: str) -> list:
    """
    Return flight times for the given destination.

    People want to know when flights for their chosen destination take off today.
    Using the functions written before, find and return the list of departure times
    (in ascending order) for that destination today.

    If there are no flights to the chosen destination, return empty list.

    :param flights: given list from database (the same as in destinations_and_times).
    :param destination: chosen destination for which we want to know the departure times.
    :return: list of departures (sorted in ascending order) for that destination.
    """
    a = []
    for i in flights:
        for j in i.split(","):
            if j == destination:
                a.append(i.split(",")[1])
    a.sort()
    return a


def flights_schedule(flights: list) -> dict:
    """
    Return flight schedule by departure times.

    Create a dictionary containing the flight schedule for the day, where the keys are the departure times
    and the values are tuples which contain the destination and the flight number
    {time1: (destination, flight_number), time2: (destination, flight_number), ...}.

    The order of the keys (departure times) is not important.

    :param flights: given list from database (the same as in destinations_and_times).
    :return: dictionary where the keys are departure times and values are tuples containing the destination and
    flight number.
    """
    a = {}

    for i in flights:
        if i.split(",")[0] not in a:
            a[i.split(",")[1]] = ()
        a[i.split(",")[1]] += (i.split(",")[0],)
        a[i.split(",")[1]] += (i.split(",")[3],)

    return a


def destinations_list(schedule: dict) -> list:
    """
    Return a list of unique destinations for the day from the given flight schedule, sorted alphabetically.

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :return: Alphabetically sorted list of unique destinations.
    """
    a = []
    o = []
    for x, y in schedule.items():
        # print(x, y)
        a.append(x)
    a.sort()
    # print(a)
    for x, y in schedule.items():
        for i in a:
            # print("x", x, "y", y, "i", i)
            if y[0] in o:
                continue
            elif i == x:
                o.append(y[0])
    o.sort()
    return o


def airlines_operating_today(schedule: dict, airline_names: dict) -> set:
    """
    Return a set of unique airline names that have flights operating today.

    Schedule is the result of the flights_schedule function.
    Airline names are presented as a dictionary where the key is the airline code
    and the value is the corresponding airline name.

    Flight code contains 3 letters and 4 numbers. The 3-letter code indicates the airline code.
    So, the 3-letter code should be taken from the airline_names dictionary (key).

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing airline codes and corresponding names.
    :return: Set of unique airline names operating today.
    """
    result = set()
    # print(airline_names)
    for q, w in airline_names.items():
        for x, y in schedule.items():
            num = len(q)
            # print("AIR", q, num)
            # print("OKAY", y[1][:num], q)
            if y[1][:num] == q:
                result.add(w)
                # print("YAY", w)
    return result


def destinations_by_airline(schedule: dict, airline_names: dict) -> dict:
    """
    Return a dictionary of destinations by airline names.

    Returns a dictionary where the keys are airline names and the values are sets of unique destinations
    that the airline is flying to today.

    Airline names is in the same format as in airlines_operating_today.
    The 3-letter code from the flight number can be used to find the airline name.

    :param schedule: Dictionary containing the flight schedule (the result of flights_schedule function).
    :param airline_names: Dictionary containing mapping of airline codes to airline names.
    :return: Dictionary of airline names to sets of destinations.
    """
    result = {}
    # print(airline_names)

    for q, w in airline_names.items():
        for x, y in schedule.items():
            num = len(q)
            if y[1][:num] == q:
                if w not in result:
                    result[w] = set()
                # print( "OK", y[1][:num], q, y[0], result[w])
                result[w].add(y[0])
                # print("YAY", result[w].add(y[0]))

    return result


if __name__ == '__main__':
    flights = [
        "Tallinn,08:00,01h30m,OWL1234",
        "Helsinki,10:35,01h00m,BHM5678",
        "Tallinn,09:00,01h30m,OWL1235",
    ]

    print(destinations_and_times(flights))
    # {'Tallinn': ['08:00', '09:00'], 'Helsinki': ['10:35']}

    flights_dict = {'Tallinn': ['09:30', '09:00'], 'Helsinki': ['10:35']}
    print(sort_dict_values(flights_dict))
    # {'Tallinn': ['09:00', '10:00'], 'Helsinki': ['10:35']}

    print(flights_to_destination(flights, "Tallinn"))
    # ['08:00', '09:00']

    print(flights_schedule(flights))
    # {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}

    schedule = {'08:00': ('Tallinn', 'OWL1234'), '10:35': ('Helsinki', 'BHM5678'), '09:00': ('Tallinn', 'OWL1235')}
    print(destinations_list(schedule))
    # ['Helsinki', 'Tallinn']

    airlines = {"OWL": "Owlbear Airlines", "BHM": "Beholder's Majesty Airlines"}

    print(airlines_operating_today(schedule, airlines))
    # {'Owlbear Airlines', "Beholder's Majesty Airlines"}

    print(destinations_by_airline(schedule, airlines))
    # {'Owlbear Airlines': {'Tallinn'}, "Beholder's Majesty Airlines": {'Helsinki'}}
