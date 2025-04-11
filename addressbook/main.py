from .utils import parse_input, save_addressbook, load_addressbook, load_notebook, save_notebook
from .address_book.handlers import add_contact, edit_contact, get_contact, birthdays, add_birthday, show_birthday, add_email, edit_email, remove_email, show_all, add_address, edit_address, remove_address
from .note_book.handlers import add_note, edit_note, delete_note, search_notes, find_note_by_tag, list_notes
from .command_matcher import match_command, KNOWN_COMMANDS, print_commands
from colorama import Fore, Style, Back

def main():
    addressbook = load_addressbook()
    notebook = load_notebook()
    print_commands()
    print()
    print(Back.CYAN + Fore.WHITE + "Welcome to the assistant bot!" + Style.RESET_ALL)
    while True:
        user_input = input(Fore.MAGENTA + "Enter a command: " + Style.RESET_ALL)
        command, *args = parse_input(user_input)

        if command not in KNOWN_COMMANDS:
            suggestion = match_command(command)
            if suggestion:
                confirm = input(f"Did you mean '{suggestion}'? (y/n): ")
                if confirm.lower() == "y":
                    command = suggestion
                else:
                    print(Fore.RED + "Unknown command." + Style.RESET_ALL)
                    return
            else:
                print(Fore.RED + "Unknown command." + Style.RESET_ALL)
                return

        match command:
            case x if x in ["close", "exit"]:
                save_data(book)
                print("Good bye!")
                break
            case "hello":
                print(Fore.MAGENTA + "How can I help you?" + Style.RESET_ALL)
            case "add":
                print(add_contact(args,addressbook))
            case "change":
                print(edit_contact(args,addressbook))
            case "phone":
                print(get_contact(args,addressbook))
            case "all":
                print(show_all(args,addressbook))
            case "add-birthday":
                print(add_birthday(args,addressbook))
            case "show-birthday":
                print(show_birthday(args,addressbook))
            case "birthdays":
                print(birthdays(args,addressbook))
            case "add-email":
                print(add_email(args,addressbook))
            case "edit-email":
                print(edit_email(args,addressbook))
            case "remove-email":
                print(remove_email(args,addressbook))
            case "add-address":
                print(add_address(args,addressbook))
            case "edit-address":
                print(edit_address(args,addressbook))
            case "remove-address":
                print(remove_address(args,addressbook))
            case "add-note":
                print(add_note(args, notebook))
            case "edit-note":
                print(edit_note(args, notebook))
            case "delete-note":
                print(delete_note(args, notebook))
            case "search-notes":
                print(search_note(args, notebook))
            case "find-note-by-tag":
                print(find_note_by_tag(args, notebook))
            case "list-notes": 
                print(list_notes(args, notebook))
            case _:
                print(Fore.RED + "Invalid command." + Style.RESET_ALL)

if __name__ == "__main__":
    main()