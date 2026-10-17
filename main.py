from datetime import datetime
concert_id=0
concert_list=[]
id_list=[]
def read_concert_data():
    """
    reads concert details from user
    artist, city, date, ticket price
    :return: (artist, city, date_obj, ticket price)
    """
    artist=input("artist: ")
    city=input("city: ")
    while True:
        date_str=input("date (YYYY-MM-DD): ")
        try:
            date_obj=datetime.strptime(date_str,"%Y-%m-%d").date()
            break
        except ValueError:
            print("Invaid date format!Use YYYY-MM-DD")

    while True:
        try:
            ticket_price=float(input("ticket_price: "))
            break
        except:
            print("Ticket price should be a number")
    return(artist,city,date_obj,ticket_price)


def create_concert(artist,city,date,ticket_price):
    """
    create a concert and generate a concert-id
    :param artist: artist name
    :param city: city name
    :param date: date name
    :param ticket_price:concert ticket price
    :return: a concert_entry
    """
    global concert_id
    concert_id+=1
    id_list.append(concert_id)
    concert_entity={"artist":artist,"city":city,"date":date,"ticket_price":ticket_price,"concert-id":concert_id}
    return concert_entity

def add_concert(concert_list,concert_entity):
    """
    adds the concert entity to the concert list
    :param concert_list: the list of all concerts
    :param concert_entity: specific concert entity

    """
    concert_list.append(concert_entity)

def add_concert_ui(concert_list):
    """
    calls the functions needed to add a concert
    :param concert_list:the list of all concerts

    """
    concert_information=read_concert_data()
    concert_dictionary=create_concert(*concert_information)
    add_concert(concert_list,concert_dictionary)

def read_data_to_modify_concert():

    """
    reads the id, the date and the ticket price which is to be modified for a concert
    :return:(id,new_date_obj, new_ticket_price)
    """
    while True:
        try:
            id_to_be_modified = int(input("id: "))
            if id_to_be_modified not in id_list:
                print(f"The concert with the id:{id_to_be_modified} was not found. Please try again.")
            else:
                break
        except ValueError:
            print("The ID must be a valid integer. Please try again.")

    while True:
        new_date_str=input("new date (YYYY-MM-DD): " )
        try:
            new_date_obj=datetime.strptime(new_date_str,"%Y-%m-%d").date()
            break
        except ValueError:
            print("Invaid date format!Use YYYY-MM-DD")
    while True:
        try:
            new_ticket_price=float(input("new_ticket_price: "))
            break
        except ValueError:
            print("Ticket price should be a number")
    return(id_to_be_modified,new_date_obj,new_ticket_price)

def modify_concert_informations(modify_id,new_date,new_ticket_price,concert_list):
    """
    modifies the informations for an existing concert
    :param modify_id: the id of the concert which is to be modified
    :param new_date: the new date of the concert
    :param new_ticket_price: the new ticket price of the concert
    :param concert_list: the list of all concert entities

    """
    for concert in concert_list:
        if(concert['concert-id']==modify_id):
            concert['date']=new_date
            concert['ticket_price']=new_ticket_price
            return




def modify_concert_informations_ui(concert_list):
    """
    calls the functions needed to modify an exisiting concert
    :param concert_list: the list of all concerts

    """
    new_concert_informations=read_data_to_modify_concert()
    modify_concert_informations(*new_concert_informations,concert_list)

def show(concert_list):
    """
    show details about all the concerts
    :param concert_list: the list of all concerts
    """
    for  concert in concert_list:
        print(f"id: {concert['concert-id']}")
        print(f"artist {concert['artist']}")
        print(f"city {concert['city']}")
        print(f"date {concert['date']}")
        print(f"ticket price {concert['ticket_price']}")
        print("")

def chose_criterion():
    """
    allows the user to chose the criterion of delete
    :return: the criterion
    """
    print("")
    print("Delete by :")
    print("artist")
    print("ticket price interval")
    print("concert date")
    print("back")
    criterion=""
    while criterion.lower() not in ['artist','ticket price interval','concert date','back']:
        print("Choose one of the criterions",end='')
        criterion=input(": ")


    return criterion.lower()
def specify_criterion(criterion):
    """
    asks the user to specify the name of the artist/the ticket price interval/the date interval based on the chosen criterion

    :param criterion: the chosen criterion
    :return: specific criterion, criterion
    """
    specific_criterion=""
    match criterion:
        case "back":
            pass
        case "artist":
            specific_criterion=input("Name of the artist to delete concerts: ")
        case "ticket price interval":
            while True:
                try:
                    lower_bound=float(input("Delete concerts with ticket prices starting from: "))
                    break
                except ValueError:
                    print("Enter a valid ticket price")
            while True:
                try:
                    upper_bound = float(input("Delete concerts with ticket prices up to: "))
                    break
                except ValueError:
                    print("Enter a valid ticket price")
            specific_criterion=(lower_bound,upper_bound)
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
            specific_criterion=(starting_date_obj, ending_date_obj)
    return specific_criterion,criterion



def delete_concerts(criterion,specific_criterion,concert_list):
    """
    deletes the concerts by the specific criterion
    :param criterion: deletes by artist/ticket price/date
    :param specific_criterion: the name of the artist or the lower/upper touple
    :param concert_list: the list of all concert
    """

    match criterion:
        case "artist":
            concert_list[:]=[concert for concert in concert_list if concert['artist']!=specific_criterion]
        case "ticket price interval":
            lower_bound,upper_bound=specific_criterion
            concert_list[:]=[concert for concert in concert_list if (concert["ticket_price"]<lower_bound or concert['ticket_price']>upper_bound)]
        case "concert date":
            lower_bound, upper_bound=specific_criterion
            concert_list[:]=[concert for concert in concert_list if not (lower_bound<concert['date']<upper_bound)]

def delete_concerts_ui(concert_list):
    """
    calls the functions needed to delete a concert
    :param concert_list: the list of all concerts

    """
    criterion=chose_criterion()
    specific_criterion,criterion=specify_criterion(criterion)
    delete_concerts(criterion,specific_criterion,concert_list)


def choose_show_criterions():
    """
    asks the user to input the criterion used to show concerts
    :return: show criterion
    """
    print("display the concerts by:")
    print("city")
    print("city and artist")
    print("artist and ticket price")
    show_criterion=''
    while show_criterion.lower() not in ['city', 'city and artist', 'artist and ticket price']:
        print("Chose a show criterion:")
        show_criterion=input(": ")
    return show_criterion.lower()

def specify_show_criterion(show_criterion):
    """
    ask the user to specify the city/city and artist/artist and maximum ticket price of the concerts he wants to display

    :param show_criterion: the chosen show criterion
    :return: the show criterion, the specific_show_criterion
    """
    match show_criterion:
        case "city":
            specific_show_criterion=input("city: ")
        case "city and artist":
            city_show=input("city: ")
            artist_show=input("artist: ")
            specific_show_criterion=(city_show,artist_show)
        case "artist and ticket price":
            artist_show = input("artist: ")
            while True:
                try:
                    ticket_price_show=float(input("maximum ticket price: "))
                except ValueError:
                    print("Enter a valid ticket price")
            specific_show_criterion = (artist_show,ticket_price_show)
    return specific_show_criterion

def show_by_criterion(show_criterion,specific_show_criterion,concert_list):
    """
    shows the concerts requested by the criterion
    :param show_criterion: the showing criterion
    :param specific_show_criterion: the specific showing criterion
    :param concert_list: the list of all concerts

    """
    match show_criterion:
        case "city":
            show_city=[c for c in concert_list if c['city']==specific_show_criterion]
            show(show_city)

        case "city and artist":
            show_city_artist = [c for c in concert_list if (c['city'] == specific_show_criterion[0] and c['artist']==specific_show_criterion[1])]
            show(show_city_artist)
        case "artist and ticket price":
            show_artist_ticket_price = [c for c in concert_list if( c['artist'] == specific_show_criterion[0] and c['ticket_price']<specific_show_criterion[1])]
            show(show_artist_ticket_price)

def show_by_criterion_ui(concert_list):
    """
    calls the functions needed to show concerts by criterion
    :param concert_list: the list of all concerts
    """
    show_criterion=choose_show_criterions()
    specific_show_criterion=specify_show_criterion(show_criterion)
    show_by_criterion(show_criterion,specific_show_criterion,concert_list)

while(True):
    print("")
    print("add, modify, delete, show" )
    print("show by criterion, exit")
    action=input("What do you want to do: ")
    match action:
        case 'add':
            add_concert_ui(concert_list)
        case 'modify':
            modify_concert_informations_ui(concert_list)
        case "show":
            show(concert_list)
        case "delete":
            delete_concerts_ui(concert_list)
        case "show by criterion":
            show_by_criterion_ui(concert_list)
        case "exit":
            exit(0)
