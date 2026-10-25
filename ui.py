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
    :param concert_list: the list of all concerts
    """
    concert_information = read_concert_data()
    try:
        concert_dictionary = logic.create_concert(*concert_information)
        logic.add_concert(concert_list, concert_dictionary)
        print("Concert added successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")


def read_data_to_modify_concert():
    """
    reads the id, the date and the ticket price which is to be modified for a concert
    :return: (id, new_date_obj, new_ticket_price)
    """
    while True:
        try:
            id_to_be_modified = int(input("id: "))
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
    if not concert_list:
        print("No concerts available to modify.")
        return
    new_concert_informations = read_data_to_modify_concert()
    try:
        logic.modify_concert_informations(*new_concert_informations, concert_list)
    except ValueError as ve:
        print(f"Error {ve}")


def show(concert_list):
    """
    show details about all the concerts
    :param concert_list: the list of all concerts
    """

    for concert in concert_list:
        print(f"id: {logic.get_id(concert)}")
        print(f"artist: {logic.get_artist(concert)}")
        print(f"city: {logic.get_city(concert)}")
        print(f"date: {logic.get_date(concert)}")
        print(f"ticket price: {logic.get_ticket_price(concert)}\n")


def chose_criterion():
    """
    allows the user to chose the criterion of delete
    :return: the criterion
    """
    print("\nDelete by :")
    print("1: artist")
    print("2: ticket price interval")
    print("3: concert date")
    print("4: back")
    criterion = ""
    while criterion not in ['1', '2', '3', '4']:
        criterion = input("Choose one of the criterions:")
    return criterion


def specify_criterion(criterion):
    """
    asks the user to specify the name of the artist/the ticket price interval/the date interval based on the chosen criterion
    for which the concerts will be deleted

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
                    upper_bound = float(input("Delete concerts with ticket prices up to: "))
                    break
                except ValueError:
                    print("Enter a valid ticket price")
            specific_criterion = (lower_bound, upper_bound)
        case "concert date":
            while True:
                starting_date = input("concerts starting from date (YYYY-MM-DD): ")
                ending_date = input("concerts up to the date (YYYY-MM-DD): ")
                try:
                    starting_date_obj = datetime.strptime(starting_date, "%Y-%m-%d").date()
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
    try:
        logic.delete_concerts(criterion, specific_criterion, concert_list)
        print("Concert deleted succesfully")
    except ValueError as ve:
        print(f"Error {ve}")


def choose_show_criterions():
    """
    asks the user to input the criterion used to show concerts
    :return: show criterion
    """
    print("Display the concerts by:")
    print("1: city")
    print("2: city and artist")
    print("3: artist and ticket price")
    show_criterion = ''
    while show_criterion not in ['1','2','3']:
        show_criterion = input("Chose a show criterion: ")
    return show_criterion


def specify_show_criterion(show_criterion):
    """
    ask the user to specify the city/city and artist/artist and maximum ticket price of the concerts he wants to display

    :param show_criterion: the chosen show criterion
    :return: specific_show_criterion
    """
    match show_criterion:
        case "1":
            specific_show_criterion = input("city: ")
        case "2":
            city_show = input("city: ")
            artist_show = input("artist: ")
            specific_show_criterion = (city_show, artist_show)
        case "3":
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
    """
    if not concert_list:
        print("No concerts available.")
        return

    show_criterion = choose_show_criterions()
    specific_show_criterion = specify_show_criterion(show_criterion)

    try:
        filtered_concerts = logic.show_by_criterion(show_criterion, specific_show_criterion, concert_list)
        show(filtered_concerts)
    except ValueError as ve:
        print(f"Error: {ve}")


def choose_report_type():
    """
    asks the user to introduce the report type
    :return:the report type
    """
    print("report type: \n 1:average ticket price for a given artist \n"
          " 2:number of concerts by city \n"
          " 3:number of concerts in a given interval,sorted by ticket price  \n"
          " 4:concerts in a given interval which take place in a given city \n"
          " 5:back")
    report_type = input(":")
    return report_type


def read_report_type(report_type):
    """
    reads the specific inputs required for the chosen report type
    :param report_type: the chosen report option
    :return: the specific inputs needed (tuple or single value), or None
    """
    match report_type:
        case "1":
            return input("Artist name: ")

        case '2' | '5':
            # No additional input needed for city report or going back
            return None

        case '3':
            while True:
                try:
                    start_str = input("Start date (YYYY-MM-DD): ")
                    start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
                    end_str = input("End date (YYYY-MM-DD): ")
                    end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
                    return (start_date, end_date)
                except ValueError:
                    print("Invalid date format! Use YYYY-MM-DD")

        case '4':
            city = input("City name: ")
            while True:
                try:
                    start_str = input("Start date (YYYY-MM-DD): ")
                    start_date = datetime.strptime(start_str, "%Y-%m-%d").date()
                    end_str = input("End date (YYYY-MM-DD): ")
                    end_date = datetime.strptime(end_str, "%Y-%m-%d").date()
                    return (city, start_date, end_date)
                except ValueError:
                    print("Invalid date format! Use YYYY-MM-DD")


def print_report_results(report_type, specific_inputs, concert_list):
    """
    calls the specific logic function and prints the results
    :param report_type: the chosen report option
    :param specific_inputs: the inputs needed for the logic function
    :param concert_list: the list of all concerts
    """
    try:
        match report_type:
            case '1':
                avg = logic.report_average_price(concert_list, specific_inputs)
                print(f"Average ticket price: {avg:.2f}")

            case '2':
                try:
                    city_report = logic.report_concerts_per_city(concert_list)
                    for city, count in city_report.items():
                        print(f"{city}: {count} concert(s)")
                except ValueError as ve:
                    print(f"Error {ve}")

            case '3':
                start_date, end_date = specific_inputs
                try:
                    interval_concerts = logic.report_concerts_in_interval(concert_list, start_date, end_date)
                    show(interval_concerts)
                except ValueError as ve:
                    print(f"Error {ve}")

            case '4':
                city, start_date, end_date = specific_inputs
                try:
                    city_interval_concerts = logic.report_concerts_in_city_and_interval(concert_list, city, start_date, end_date)
                    show(city_interval_concerts)
                except ValueError as ve:
                    print(f"Error {ve}")

            case _:
                print("Invalid report type. Please try again.")

    except ValueError as ve:
        print(f"Report Error: {ve}")


def report_ui(concert_list):
    """
    calls the functions needed for reports
    :param concert_list: the list of all concerts
    """
    if not concert_list:
        print("No concerts available for reporting.")
        return

    report_type = choose_report_type()

    if report_type == '5':
        return

    specific_inputs = read_report_type(report_type)
    print_report_results(report_type, specific_inputs, concert_list)