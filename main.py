import ui


def main():
    concert_list = []

    while True:
        print("\n--- Menu ---")
        print("1. Add concert")
        print("2. Modify concert")
        print("3. Delete concert")
        print("4. Show all concerts")
        print("5. Show by criterion")
        print("6. Report")
        print("7. Exit")

        action = input("What do you want to do (enter a number): ").strip()

        match action:
            case '1':
                ui.add_concert_ui(concert_list)
            case '2':
                ui.modify_concert_informations_ui(concert_list)
            case '3':
                ui.delete_concerts_ui(concert_list)
            case '4':
                ui.show(concert_list)
            case '5':
                ui.show_by_criterion_ui(concert_list)
            case '6':
                ui.report_ui(concert_list)
            case '7':
                print("Exiting program...")
                break
            case _:
                print("Invalid command. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()