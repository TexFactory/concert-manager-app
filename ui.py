from datetime import datetime
import logic


def read_concert_data():
    """
    reads concert details from user
    artist, city, date, ticket price
    :return: (artist, city, date_obj, ticket price)
    """
    artist = input("artist: ")
    city = input("city: ")
    while True:
        date_str = input("date (YYYY-MM-DD): ")
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invaid date format!Use YYYY-MM-DD")

    while True:
        try:
            ticket_price = float(input("ticket_price: "))
            break
        except ValueError:
            print("Ticket price should be a number")
    return (artist, city, date_obj, ticket_price)


def add_concert_ui(concert_list):
    """
    calls the functions needed to add a concert
    :param concert_list:the list of all concerts

    """
    concert_information = read_concert_data()
    concert_dictionary = logic.create_concert(*concert_information)
    logic.add_concert(concert_list, concert_dictionary)


def read_data_to_modify_concert():
    """
    reads the id, the date and the ticket price which is to be modified for a concert
    :return:(id,new_date_obj, new_ticket_price)
    """
    while True:
        try:
            id_to_be_modified = int(input("id: "))
            if id_to_be_modified not in logic.id_list:
                print(f"The concert with the id:{id_to_be_modified} was not found. Please try again.")
            else:
                break
        except ValueError:
            print("The ID must be a valid integer. Please try again.")

    while True:
        new_date_str = input("new date (YYYY-MM-DD): ")
        try:
            new_date_obj = datetime.strptime(new_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invaid date format!Use YYYY-MM-DD")

    while True:
        try:
            new_ticket_price = float(input("new_ticket_price: "))
            break
        except ValueError:
            print("Ticket price should be a number")

    return (id_to_be_modified, new_date_obj, new_ticket_price)


def modify_concert_informations_ui(concert_list):
    """
    calls the functions needed to modify an exisiting concert
    :param concert_list: the list of all concerts

    """
    new_concert_informations = read_data_to_modify_concert()
    logic.modify_concert_informations(*new_concert_informations, concert_list)


def show(concert_list):
    """
    show details about all the concerts
    :param concert_list: the list of all concerts
    """
    if not concert_list:
        print("No concerts found.")
        return
    for concert in concert_list:
        print(f"id: {concert['concert-id']}")
        print(f"artist {concert['artist']}")
        print(f"city {concert['city']}")
        print(f"date {concert['date']}")
        print(f"ticket price {concert['ticket_price']}\n")


def chose_criterion():
    """
    allows the user to chose the criterion of delete
    :return: the criterion
    """
    print("\nDelete by :")
    print("artist")
    print("ticket price interval")
    print("concert date")
    print("back")
    criterion = ""
    while criterion.lower() not in ['artist', 'ticket price interval', 'concert date', 'back']:
        print("Choose one of the criterions: ", end='')
        criterion = input()
    return criterion.lower()


def specify_criterion(criterion):
    """
    asks the user to specify the name of the artist/the ticket price interval/the date interval based on the chosen criterion

    :param criterion: the chosen criterion
    :return: specific criterion, criterion
    """
    specific_criterion = ""
    match criterion:
        case "back":
            pass
        case "artist":
            specific_criterion = input("Name of the artist to delete concerts: ")
        case "ticket price interval":
            while True:
                try:
                    lower_bound = float(input("Delete concerts with ticket prices starting from: "))
                    break
                except ValueError:
                    print("Enter a valid ticket price")
            while True:
                try:
                    upper_bound = float(input("Delete concerts with ticket prices up to: "))
                    break
                except ValueError:
                    print("Enter a valid ticket price")
            specific_criterion = (lower_bound, upper_bound)
        case "concert date":
            while True:
                starting_date = input("concerts starting from date (YYYY-MM-DD): ")
                try:
                    starting_date_obj = datetime.strptime(starting_date, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invaid date format!Use YYYY-MM-DD")

            while True:
                ending_date = input("concerts up to the date (YYYY-MM-DD): ")
                try:
                    ending_date_obj = datetime.strptime(ending_date, "%Y-%m-%d").date()
                    break
                except ValueError:
                    print("Invaid date format!Use YYYY-MM-DD")
            specific_criterion = (starting_date_obj, ending_date_obj)

    return specific_criterion, criterion


def delete_concerts_ui(concert_list):
    """
    calls the functions needed to delete a concert
    :param concert_list: the list of all concerts

    """
    criterion = chose_criterion()
    if criterion == "back":
        return
    specific_criterion, criterion = specify_criterion(criterion)
    logic.delete_concerts(criterion, specific_criterion, concert_list)


def choose_show_criterions():
    """
    asks the user to input the criterion used to show concerts
    :return: show criterion
    """
    print("display the concerts by:")
    print("city")
    print("city and artist")
    print("artist and ticket price")
    show_criterion = ''
    while show_criterion.lower() not in ['city', 'city and artist', 'artist and ticket price']:
        show_criterion = input("Chose a show criterion: ")
    return show_criterion.lower()


def specify_show_criterion(show_criterion):
    """
    ask the user to specify the city/city and artist/artist and maximum ticket price of the concerts he wants to display

    :param show_criterion: the chosen show criterion
    :return: the show criterion, the specific_show_criterion
    """
    match show_criterion:
        case "city":
            specific_show_criterion = input("city: ")
        case "city and artist":
            city_show = input("city: ")
            artist_show = input("artist: ")
            specific_show_criterion = (city_show, artist_show)
        case "artist and ticket price":
            artist_show = input("artist: ")
            while True:
                try:
                    ticket_price_show = float(input("maximum ticket price: "))
                    break
                except ValueError:
                    print("Enter a valid ticket price")
            specific_show_criterion = (artist_show, ticket_price_show)
    return specific_show_criterion


def show_by_criterion_ui(concert_list):
    """
    calls the functions needed to show concerts by criterion
    :param concert_list: the list of all concerts
    """
    show_criterion = choose_show_criterions()
    specific_show_criterion = specify_show_criterion(show_criterion)
    filtered_concerts = logic.show_by_criterion(show_criterion, specific_show_criterion, concert_list)
    show(filtered_concerts)

