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

def modify_concert_informations(modify_id, new_date, new_ticket_price, concert_list):
    """
    modifies the informations for an existing concert
    :param modify_id: the id of the concert which is to be modified
    :param new_date: the new date of the concert
    :param new_ticket_price: the new ticket price of the concert
    :param concert_list: the list of all concert entities

    """
    for concert in concert_list:
        if concert['concert-id'] == modify_id:
            concert['date'] = new_date
            concert['ticket_price'] = new_ticket_price
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
            concert_list[:] = [concert for concert in concert_list if concert['artist'] != specific_criterion]
        case "ticket price interval":
            lower_bound, upper_bound = specific_criterion
            concert_list[:] = [concert for concert in concert_list if (concert["ticket_price"] < lower_bound or concert['ticket_price'] > upper_bound)]
        case "concert date":
            lower_bound, upper_bound = specific_criterion
            concert_list[:] = [concert for concert in concert_list if not (lower_bound < concert['date'] < upper_bound)]

def show_by_criterion(show_criterion, specific_show_criterion, concert_list):
    """
    shows the concerts requested by the criterion
    :param show_criterion: the showing criterion
    :param specific_show_criterion: the specific showing criterion
    :param concert_list: the list of all concerts

    """
    match show_criterion:
        case "city":
            return [c for c in concert_list if c['city'] == specific_show_criterion]
        case "city and artist":
            return [c for c in concert_list if (c['city'] == specific_show_criterion[0] and c['artist'] == specific_show_criterion[1])]
        case "artist and ticket price":
            return [c for c in concert_list if (c['artist'] == specific_show_criterion[0] and c['ticket_price'] < specific_show_criterion[1])]
    return []