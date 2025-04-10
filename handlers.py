from error_handler import input_error, EmailValidationError
from address_book import Record, AddressBook, Email

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
def get_contact(args, book: AddressBook): #changed the argument to the book: AddressBook
    name = args[0]
    record = book.find(name)
    return f"{name}: {', '.join(p.value for p in record.phones)}" #now it rerurns name and all phone numbers

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
    name = args[0]
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
    name = args[0]
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."

    if not hasattr(record, "emails") or not record.emails:
        return f"No email found for contact '{name}' to edit."

    # Replace the first email
    record.emails[0] = Email(new_email)
    return f"Email updated for contact '{name}'."

@input_error
def show_all(book):
    """Displays all contacts with their phone numbers."""
    if not book.data:
        return "The address book is empty."
    return "\n".join(str(record) for record in book.data.values())

