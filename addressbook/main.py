from .utils import parse_input, save_data, load_data
from .handlers import add_contact, edit_contact, get_contact, birthdays, add_birthday, show_birthday, add_email, edit_email, show_all, remove_email, show_all, add_address, edit_address, remove_address
from .address_book import AddressBook
from .command_matcher import match_command, KNOWN_COMMANDS

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command not in KNOWN_COMMANDS:
            suggestion = match_command(command)
            if suggestion:
                confirm = input(f"Did you mean '{suggestion}'? (y/n): ")
                if confirm.lower() == "y":
                    command = suggestion
                else:
                    print("Unknown command.")
                    return
            else:
                print("Unknown command.")
                return

        match command:
            case x if x in ["close", "exit"]:
                save_data(book)
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(edit_contact(args, book))
            case "phone":
                print(get_contact(args, book))
            case "all":
                print(show_all(args, book))
            case "add-birthday":
                print(add_birthday(args, book))
            case "show-birthday":
                print(show_birthday(args, book))
            case "birthdays":
                print(birthdays(args, book))
            case "add-email":
                print(add_email(args, book))
            case "edit-email":
                print(edit_email(args, book))
            case "remove-email":
                print(remove_email(args, book))
            case "add-address":
                print(add_address(args, book))
            case "edit-address":
                print(edit_address(args, book))
            case "remove-address":
                print(remove_address(args, book))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()