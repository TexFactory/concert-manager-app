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

    if not artist.strip():
        raise ValueError("Artist name cannot be empty.")
    if not city.strip():
        raise ValueError("City name cannot be empty.")
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
    if new_ticket_price < 0:
        raise ValueError("Ticket price cannot be negative")
    concert["ticket_price"] = new_ticket_price

def modify_concert_informations(modify_id, new_date, new_ticket_price, concert_list):
    """
    modifies the informations for an existing concert
    :param modify_id: the id of the concert which is to be modified
    :param new_date: the new date of the concert
    :param new_ticket_price: the new ticket price of the concert
    :param concert_list: the list of all concert entities

    """
    if new_ticket_price < 0:
        raise ValueError("Ticket price cannot be negative.")
    for concert in concert_list:
        if get_id(concert) == modify_id:
            set_date(concert,new_date)
            set_ticket_price(concert,new_ticket_price)
            return
    raise ValueError(f"Concert with ID{modify_id} does not exist")

def delete_concerts(criterion, specific_criterion, concert_list):
    """
    deletes the concerts by the specific criterion and the coresponding id from id list
    :param criterion: deletes by artist/ticket price/date
    :param specific_criterion: the name of the artist or the lower/upper touple
    :param concert_list: the list of all concert
    """
    initial_length = len(concert_list)

    match criterion:
        case "1":
            concert_list[:] = [c for c in concert_list if get_artist(c) != specific_criterion]
        case "2":
            lower_bound, upper_bound = specific_criterion
            if lower_bound > upper_bound:
                raise ValueError("Lower bound cannot be greater than upper bound.")
            concert_list[:] = [c for c in concert_list if not (lower_bound <= get_ticket_price(c) <= upper_bound)]
        case "3":
            lower_bound, upper_bound = specific_criterion
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
            return [c for c in concert_list if (get_city(c) == specific_show_criterion[0] and get_artist(c) == specific_show_criterion[1])]
        case "3":
            return [c for c in concert_list if (get_artist(c) == specific_show_criterion[0] and get_ticket_price(c) < specific_show_criterion[1])]
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