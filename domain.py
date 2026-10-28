import datetime


def create_concert(artist, city, date, ticket_price,concert_id):
    """
    create a concert and generate a concert-id
    :param artist: artist name
    :param city: city name
    :param date: date name
    :param ticket_price:concert ticket price
    :param concert_id:the concert id
    :return: a concert_entry
    """

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

    concert_entity = [
         artist,
         city,
         date,
         ticket_price,
         concert_id
    ]
    return concert_entity

def get_id(concert):
    """
    gets the id of a concert entity
    :param concert: specific concert entity
    :return: concert id
    """
    return concert[4]


def get_artist(concert):
    """
    gets the artist of a concert entity
    :param concert: specific concert entity
    :return: artist name
    """
    return concert[0]


def get_city(concert):
    """
    gets the city of a concert entity
    :param concert: specific concert entity
    :return: city name
    """
    return concert[1]


def get_date(concert):
    """
    gets the date of a concert entity
    :param concert: specific concert entity
    :return: concert date
    """
    return concert[2]


def get_ticket_price(concert):
    """
    gets the ticket price of a concert entity
    :param concert: specific concert entity
    :return: ticket price
    """
    return concert[3]


def set_date(concert, new_date):
    """
    sets the new date for a concert entity
    :param concert: specific concert entity
    :param new_date: the new date of the concert
    """
    concert[2] = new_date


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
    concert[3] = float(new_ticket_price)