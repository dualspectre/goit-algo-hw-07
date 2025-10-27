from AddressBook import *

# Decorator for handling input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return f"{ve}"
        except IndexError:
            return "Not enough arguments provided."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner

#function of parsing user input command
@input_error
def parse_input(user_input): 
    """
    Parses the user input command and returns the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#function of adding a contact
@input_error
def add_contact(args, book: AddressBook) -> str:
    """
    Adds a new contact to the contacts dictionary.
    Input: args - list of arguments, contacts - dictionary of contacts

    Return: message - status of add operation
    """
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

#function of changing a contact
@input_error
def change_contact(args, book: AddressBook) -> str:
    """
    Changes an existing contact in the AddressBook.
    Input: args - list of arguments, book - AddressBook instance

    Return: str - status of change operation
    """
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    else:
        record.edit_phone(old_phone, new_phone)
        return "Contact changed."
    

#function of showing a contact's phone number
@input_error
def show_phone_number(args, book: AddressBook) -> str:
    """
    Shows a contact's phone number.
    Input: args - list of arguments, book - AddressBook instance

    Return: str - the contact's phone number or an error message
    """
    name = args[0]
    return f"{name}: {[str(phone) for phone in book.data[name].phones]}"

@input_error
# function of adding a birthday to a contact
def add_birthday(args, book: AddressBook):
    """
    Adds a birthday to a contact.
    Input: args - list of arguments, book - AddressBook instance

    Return: str - status of adding birthday operation
    """
    name, birthday, *_ = args
    if name not in book.data:
        raise KeyError
    else:
        book.data[name].add_birthday(birthday)
        return "Birthday added."

@input_error
# function of showing a contact's birthday
def show_birthday(args, book: AddressBook):
    """
    Shows a contact's birthday.
    input: args - list of arguments, book - AddressBook instance
    Return: str - the contact's birthday or an error message
    """
    name, *_ = args
    record = book.find(name)
    if record is None:
        raise KeyError
    else:
        return f"{name}: {record.birthday}"

@input_error
# function of showing upcoming birthdays
def birthdays(args, book: AddressBook):
    """
    Shows upcoming birthdays from the AddressBook.
    Input: args - list of arguments, book - AddressBook instance

    Return: str - upcoming birthdays or an error message
    """
    return book.get_upcoming_birthdays()

#function of showing all contacts
def show_all_contacts(book: AddressBook) -> str:
    """
    Shows all contacts in the contacts dictionary.
    Input: contacts - dictionary of contacts

    Return: str - all contacts or an error message
    """
    return str(book)