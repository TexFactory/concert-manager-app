import ui
def main():
    concert_list = []

    while True:
        print("\nadd, modify, delete, show")
        print("show by criterion, report, exit")
        action = input("What do you want to do: ").strip().lower()

        match action:
            case 'add':
                ui.add_concert_ui(concert_list)
            case 'modify':
                ui.modify_concert_informations_ui(concert_list)
            case "show":
                ui.show(concert_list)
            case "delete":
                ui.delete_concerts_ui(concert_list)
            case "show by criterion":
                ui.show_by_criterion_ui(concert_list)
            case "exit":
                print("Exiting program...")
                break
            case "report":
                pass
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()