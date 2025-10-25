from AddressBook import AddressBook
import handler


def main():
    print("Welcome to the Phone Bot!")
    book = AddressBook()

    while True:
        user_input = input("Please enter a command: ")
        
        cmd, *args = handler.parse_input(user_input)

        # Command handling
        if cmd in ["exit", "close"]:
            print("Good bye!")
            break
            # hello command actions
        elif cmd == "hello":
            print("Hello! Can i help you")
        
        # add command actions
        elif cmd == "add":
            print(handler.add_contact(args, book))
        
        # change command actions                
        elif cmd == "change":
            print(handler.change_contact(args, book))
                
            # phone command actions
        elif cmd == "phone":
            print(handler.show_phone_number(args, book))
        
        # all command actions
        elif cmd == "all":
            print(handler.show_all_contacts(book))

        elif cmd == "add-birthday":
            print(handler.add_birthday(args, book))

        elif cmd == "show-birthday":
            print(handler.show_birthday(args, book))

        elif cmd == "birthdays":
            print(handler.birthdays(args, book))

            # help command actions
        elif cmd == "help":
            print("\nAvailable commands: add, change, phone, add-birthday, show-birthday, birthdays, all, exit, close\
                \nadd <name> <phone> - add a new contact or new phone number in current contact in address book\
                \nchange <name> <old_phone> <new_phone> - change an existing contact phone number\
                \nphone <name> - show a contact's phone number\
                \nall - show all contacts\
                \nadd-birthday <name> <birthday> - add a birthday for a contact\
                \nshow-birthday <name> - show a contact's birthday\
                \nbirthdays - show upcoming birthdays\
                \nclose, exit - close the application\
                \n<phone> must have 10 digits and can started with +")
        
        # unknown command actions
        else:
            print("Unknown command")
        

if __name__ == "__main__":
    main()

