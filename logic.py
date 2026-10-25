concert_id = 0

import datetime
def create_concert(artist, city, date, ticket_price):
    """
    create a concert and generate a concert-id
    :param artist: artist name
    :param city: city name
    :param date: date name
    :param ticket_price:concert ticket price
    :return: a concert_entry
    """
    global concert_id

    if not isinstance(artist, str) or not artist.strip():
        raise ValueError("Artist name cannot be empty.")
    if not isinstance(city, str) or not city.strip():
        raise ValueError("City name cannot be empty.")
    if not isinstance(date, datetime.date):
        raise ValueError("Date must be a valid datetime.date object.")
    if not isinstance(ticket_price, (int, float)):
        raise ValueError("Ticket price must be a number.")
    if ticket_price < 0:
        raise ValueError("Ticket price cannot be negative.")

    concert_id += 1
    concert_entity = {
        "artist": artist,
        "city": city,
        "date": date,
        "ticket_price": ticket_price,
        "concert-id": concert_id
    }
    return concert_entity

def add_concert(concert_list, concert_entity):
    """
    adds the concert entity to the concert list
    :param concert_list: the list of all concerts
    :param concert_entity: specific concert entity

    """
    concert_list.append(concert_entity)
def get_id(concert):
    """
    gets the id of a concert entity
    :param concert: specific concert entity
    :return: concert id
    """
    return concert["concert-id"]


def get_artist(concert):
    """
    gets the artist of a concert entity
    :param concert: specific concert entity
    :return: artist name
    """
    return concert["artist"]


def get_city(concert):
    """
    gets the city of a concert entity
    :param concert: specific concert entity
    :return: city name
    """
    return concert["city"]


def get_date(concert):
    """
    gets the date of a concert entity
    :param concert: specific concert entity
    :return: concert date
    """
    return concert["date"]


def get_ticket_price(concert):
    """
    gets the ticket price of a concert entity
    :param concert: specific concert entity
    :return: ticket price
    """
    return concert["ticket_price"]


def set_date(concert, new_date):
    """
    sets the new date for a concert entity
    :param concert: specific concert entity
    :param new_date: the new date of the concert
    """
    concert["date"] = new_date


def set_ticket_price(concert, new_ticket_price):
    """
    sets the new ticket price for a concert entity
    :param concert: specific concert entity
    :param new_ticket_price: the new ticket price of the concert
    """
    if not isinstance(new_ticket_price, (int, float)):
        raise ValueError("Ticket price must be a number.")
    if new_ticket_price < 0:
        raise ValueError("Ticket price cannot be negative.")
    concert["ticket_price"] = float(new_ticket_price)

def modify_concert_informations(modify_id, new_date, new_ticket_price, concert_list):
    """
    modifies the informations for an existing concert
    :param modify_id: the id of the concert which is to be modified
    :param new_date: the new date of the concert
    :param new_ticket_price: the new ticket price of the concert
    :param concert_list: the list of all concert entities

    """
    if not isinstance(new_ticket_price, (int, float)) or new_ticket_price < 0:
        raise ValueError("Ticket price must be a valid positive number.")
    if not isinstance(new_date, datetime.date):
        raise ValueError("Date must be a valid datetime.date object.")

    for concert in concert_list:
        if get_id(concert) == modify_id:
            set_date(concert, new_date)
            set_ticket_price(concert, new_ticket_price)
            return
    raise ValueError(f"Concert with ID {modify_id} does not exist.")
def delete_concerts(criterion, specific_criterion, concert_list):
    """
    deletes the concerts by the specific criterion and the coresponding id from id list
    :param criterion: deletes by artist/ticket price/date
    :param specific_criterion: the name of the artist or the lower/upper touple
    :param concert_list: the list of all concert
    """

    initial_length = len(concert_list)

    match criterion:
        case "artist":
            concert_list[:] = [c for c in concert_list if get_artist(c) != specific_criterion]
        case "ticket price interval":
            lower_bound, upper_bound = specific_criterion
            if not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):
                raise ValueError("Ticket price bounds must be numbers.")
            if lower_bound < 0 or upper_bound < 0:
                raise ValueError("Ticket prices cannot be negative.")
            if lower_bound > upper_bound:
                raise ValueError("Lower bound cannot be greater than upper bound.")

            concert_list[:] = [c for c in concert_list if not (lower_bound <= get_ticket_price(c) <= upper_bound)]
        case "concert date":
            lower_bound, upper_bound = specific_criterion
            if not isinstance(lower_bound, datetime.date) or not isinstance(upper_bound, datetime.date):
                raise ValueError("Date bounds must be valid datetime.date objects.")
            if lower_bound > upper_bound:
                raise ValueError("Starting date cannot be after ending date.")

            concert_list[:] = [c for c in concert_list if not (lower_bound <= get_date(c) <= upper_bound)]

    if len(concert_list) == initial_length:
        raise ValueError("No concerts matched the criteria for deletion.")

def show_by_criterion(show_criterion, specific_show_criterion, concert_list):
    """
    shows the concerts requested by the criterion
    :param show_criterion: the showing criterion
    :param specific_show_criterion: the specific showing criterion
    :param concert_list: the list of all concerts

    """
    match show_criterion:
        case "1":
            return [c for c in concert_list if get_city(c) == specific_show_criterion]
        case "2":
            return [c for c in concert_list if
                    (get_city(c) == specific_show_criterion[0] and get_artist(c) == specific_show_criterion[1])]
        case "3":
            artist, max_price = specific_show_criterion
            if not isinstance(max_price, (int, float)) or max_price < 0:
                raise ValueError("Maximum ticket price must be a valid positive number.")
            return [c for c in concert_list if (get_artist(c) == artist and get_ticket_price(c) <= max_price)]
    return []



def report_average_price(concert_list, artist):
    """
    function that returns the average price of concerts for a given artist
    :param concert_list:the list of all concerts
    :param artist:specific artist
    :return:the average price of concerts for a given artist
    """
    sum=0
    count=0
    for concert in concert_list:
        if(get_artist(concert)==artist):
            count+=1
            sum+=get_ticket_price(concert)

    if count==0:
        raise ValueError(f"No concerts found for artist {artist}")
    return sum/count


def report_concerts_per_city(concert_list):
    """
    function that returns the number of concerts in each city
    :param concert_list: the list of all concerts
    :return: a dictionary of the number of concerts in every city
    """
    concert_by_city={}
    for concert in concert_list:
        city=get_city(concert)
        concert_by_city[city]= concert_by_city.get(city,0)+1
    if not concert_by_city:
        raise ValueError(f"No concerts available for report")
    return concert_by_city

def report_concerts_in_interval(concert_list, start_date, end_date):
    """
    a function that returns the concert in a given date interval, sorted by ascending ticket price
    :param concert_list: the list of all  concerts
    :param start_date: starting date of the shown concerts
    :param end_date: ending date of the shown concerts
    """
    if start_date>end_date:
        raise ValueError('Start date cannot be after end date')
    filtered=[concert for concert in concert_list if start_date <= get_date(concert) <= end_date ]
    return sorted(filtered,key=get_ticket_price)

def report_concerts_in_city_and_interval(concert_list, city, start_date, end_date):
    """
       a function that returns the concert in a given date interval, in a given city
       :param concert_list: the list of all  concerts
       :param city the given city
       :param start_date: starting date of the shown concerts
       :param end_date: ending date of the shown concerts
       """
    if start_date > end_date:
        raise ValueError('Start date cannot be after end date')
    filtered = [concert for concert in concert_list if start_date <= get_date(concert) <= end_date and get_city(concert)==city]
    return filtered

