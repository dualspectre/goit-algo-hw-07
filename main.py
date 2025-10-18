from collections import UserDict
import handler

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self,value):
        if value.isdigit() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Phone number must be exactly 10 digits")
        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Method to add a phone number
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Method to remove a phone number
    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    # Method to edit a phone number
    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return
        raise ValueError("Old phone number not found")
    
    # Method to find a phone number
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())


def main():
    print("Welcome to the Phone Bot!")
    contacts = {}

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
            print(handler.add_contact(args, contacts))
        
        # change command actions                
        elif cmd == "change":
            print(handler.change_contact(args, contacts))
                
            # phone command actions
        elif cmd == "phone":
            print(handler.show_phone_number(args, contacts))
        
        # all command actions
        elif cmd == "all":
            print(handler.show_all_contacts(contacts))
            
            # help command actions
        elif cmd == "help":
            print("\nAvailable commands: add, change, phone, all, exit, close\
                \nadd <name> <phone> - add a new contact\
                \nchange <name> <phone> - change an existing contact\
                \nphone <name> - show a contact's phone number\
                \nall - show all contacts\
                \nclose, exit - close the application\
                \n<phone> must have 9-12 digits and can started with +")
        
        # unknown command actions
        else:
            print("Unknown command")
        

if __name__ == "__main__":
    main()

