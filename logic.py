concert_id = 0
id_list = []

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
    concert_id += 1
    id_list.append(concert_id)
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
    concert["ticket_price"] = new_ticket_price

def modify_concert_informations(modify_id, new_date, new_ticket_price, concert_list):
    """
    modifies the informations for an existing concert
    :param modify_id: the id of the concert which is to be modified
    :param new_date: the new date of the concert
    :param new_ticket_price: the new ticket price of the concert
    :param concert_list: the list of all concert entities

    """
    for concert in concert_list:
        if get_id(concert) == modify_id:
            set_date(concert,new_date)
            set_ticket_price(concert,new_ticket_price)
            return

def delete_concerts(criterion, specific_criterion, concert_list):
    """
    deletes the concerts by the specific criterion
    :param criterion: deletes by artist/ticket price/date
    :param specific_criterion: the name of the artist or the lower/upper touple
    :param concert_list: the list of all concert
    """
    match criterion:
        case "artist":
            concert_list[:] = [concert for concert in concert_list if get_artist(concert) != specific_criterion]
        case "ticket price interval":
            lower_bound, upper_bound = specific_criterion
            concert_list[:] = [concert for concert in concert_list if
                               (get_ticket_price(concert) < lower_bound or get_ticket_price(concert) > upper_bound)]
        case "concert date":
            lower_bound, upper_bound = specific_criterion
            concert_list[:] = [concert for concert in concert_list if
                               not (lower_bound < get_date(concert) < upper_bound)]



def show_by_criterion(show_criterion, specific_show_criterion, concert_list):
    """
    shows the concerts requested by the criterion
    :param show_criterion: the showing criterion
    :param specific_show_criterion: the specific showing criterion
    :param concert_list: the list of all concerts

    """
    match show_criterion:
        case "city":
            return [c for c in concert_list if get_city(c) == specific_show_criterion]
        case "city and artist":
            return [c for c in concert_list if (get_city(c) == specific_show_criterion[0] and get_artist(c) == specific_show_criterion[1])]
        case "artist and ticket price":
            return [c for c in concert_list if (get_artist(c) == specific_show_criterion[0] and get_ticket_price(c) < specific_show_criterion[1])]
    return []

