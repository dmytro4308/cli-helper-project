from .error_handler import input_error, EmailValidationError, EmailIsNotFound
from .address_book import Record, AddressBook, Email

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def edit_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if not record.edit_phone(old_phone, new_phone):
        return f"Phone number {old_phone} not found for contact {name}."
    return f"Phone number updated for contact {name}."

@input_error
def get_contact(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    return f"{name}: {', '.join(p.value for p in record.phones)}"

@input_error
def add_birthday(args, book):
    name, bday_str, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_birthday(bday_str)
    return "Birthday added."

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    if record.birthday:
        return record.birthday.value.strftime("%d.%m.%Y")
    return "Birthday not set."

@input_error
def birthdays(args, book):
    try:
        days = int(args[0]) if args else 7
    except ValueError:
        return "Please enter a valid number of days."

    upcoming = book.get_upcoming_birthdays(days)
    if not upcoming:
        return f"No birthdays in the upcoming {days} days."
    return "\n".join(
        f"{item['name']}: {item['congratulation_date']}" for item in upcoming
    )

@input_error
def add_email(args, book: AddressBook):
    if len(args) < 2:
        raise EmailValidationError
    name, email_str, *_ = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_email(email_str)
    return f"Email added to contact {name}."

@input_error
def edit_email(args, book: AddressBook):
    if len(args) < 2:
        return "Error: Provide both a name and an email."
    name, new_email, *_ = args
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."

    record.edit_email(new_email)
    return f"Email updated for contact '{name}'."

@input_error 
def remove_email(args, book: AddressBook):
    if len(args) < 1:
        return "Error: Provide a name and email witch need to be deleted."
    name, email, *_ = args
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."

    try:
        record.remove_email(email)
        return f"Email '{email}' removed from contact '{name}'."
    except EmaiIsNotFound:
        return "Email is not found"

@input_error
def add_address(args, book: AddressBook):
    if len(args) < 2:
        raise EmailValidationError
    name, *address_parts = args
    address = ' '.join(address_parts)
    record = book.find(name)
    if record is None:
        return "Contact not found."
    record.add_address(address)
    return f"Address added to contact {name}."

@input_error
def edit_address(args, book: AddressBook):
    if len(args) < 2:
        return "Error: Provide both a name and an address."
    name, *address_parts = args
    address = ' '.join(address_parts)
    record = book.find(name)
    if record is None:
        return f"Contact '{name}' not found."

    record.edit_address(address)
    return f"Address updated for contact '{name}'."

@input_error 
def remove_address(args, book: AddressBook):
    if len(args) < 1:
        return "Error: Provide a name and address witch need to be deleted."
    name, address, *_ = args
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."

    try:
        record.remove_address(address)
        return f"Address '{address}' removed from contact '{name}'."
    except EmaiIsNotFound:
        return "Address is not found"


@input_error
def show_all(args, book):
    """Displays all contacts with their phone numbers."""
    if not book.data:
        return "The address book is empty."
    return "\n".join(str(record) for record in book.data.values())