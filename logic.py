import datetime

from domain import (
    create_concert,
    get_id,
    get_artist,
    get_city,
    get_date,
    get_ticket_price,
    set_date,
    set_ticket_price,
)

def add_concert(concert_list, concert_entity):
    """
    adds the concert entity to the concert list
    :param concert_list: the list of all concerts
    :param concert_entity: specific concert entity

    """
    concert_list.append(concert_entity)

def get_next_id(concert_list):
    """
    generates the next available ID dynamically based on the current concert list
    :param concert_list: list of all concerts
    :return: next integer ID
    """
    if not concert_list:
        return 1
    return max(get_id(c) for c in concert_list) + 1


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
        case "1":
            concert_list[:] = [c for c in concert_list if get_artist(c) != specific_criterion]
        case "2":
            lower_bound, upper_bound = specific_criterion
            if not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):
                raise ValueError("Ticket price bounds must be numbers.")
            if lower_bound < 0 or upper_bound < 0:
                raise ValueError("Ticket prices cannot be negative.")
            if lower_bound > upper_bound:
                raise ValueError("Lower bound cannot be greater than upper bound.")

            concert_list[:] = [c for c in concert_list if not (lower_bound <= get_ticket_price(c) <= upper_bound)]
        case "3":
            lower_bound, upper_bound = specific_criterion
            if not isinstance(lower_bound, datetime.date) or not isinstance(upper_bound, datetime.date):
                raise ValueError("Date bounds must be valid datetime.date objects.")
            if lower_bound > upper_bound:
                raise ValueError("Starting date cannot be after ending date.")

            concert_list[:] = [c for c in concert_list if not (lower_bound <= get_date(c) <= upper_bound)]
        case "4":

            artist_name_list,maximum_ticket_price=specific_criterion
            if not isinstance(maximum_ticket_price, (int,float)):
                raise ValueError("Ticket prices must be numbers")
            if maximum_ticket_price<0:
                raise ValueError('Ticket prices cannot be negative')
            concert_list[:] = [
                c
                for c in concert_list
                if not (
                        get_artist(c) in artist_name_list
                        and get_ticket_price(c) > maximum_ticket_price
                )
            ]

        case '5':
            maximum_ticket_price,latest_date=specific_criterion
            if not isinstance(maximum_ticket_price, (int,float)):
                raise ValueError("Ticket prices must be numbers")
            if maximum_ticket_price<0:
                raise ValueError('Ticket prices cannot be negative')
            if not isinstance(latest_date, datetime.date):
                raise ValueError("Date bounds must be valid datetime.date objects.")
            concert_list[:]=[concert for concert in concert_list if not (get_ticket_price(concert)>maximum_ticket_price or get_date(concert)>latest_date)]
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
    suma=0
    count=0
    for concert in concert_list:
        if(get_artist(concert)==artist):
            count+=1
            suma+=get_ticket_price(concert)

    if count==0:
        raise ValueError(f"No concerts found for artist {artist}")
    return suma/count

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

def copy_concert_list(concert_list):
    """
    a function that returns a copy of the current concert list
    :param concert_list:the list of all concerts
    :return:copy of the list of all curent concerts
    """
    return [c[:] for c in concert_list]