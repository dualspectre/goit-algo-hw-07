from collections import UserDict
from datetime import datetime, date, timedelta

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

class Birthday(Field):

    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%Y.%m.%d").date()
        except ValueError:
            raise ValueError("Use YYYY.MM.DD format")
    
    def __str__(self):
        return self.value.strftime("%Y.%m.%d")    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # Method to add a phone number
    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    # Method to remove a phone number
    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone:
            self.phones.remove(found_phone)
        else:
            raise ValueError("Phone number not found")

    # Method to edit a phone number
    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
        
    
    # Method to find a phone number
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self, birthday : str):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = ', '.join(str(phone) for phone in self.phones)
        return f"name: {self.name.value}, phones: {phones}, birthday: {self.birthday.value if self.birthday else 'N/A'}"

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __find_next_weekday(self, start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def __adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self.__find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = date.today()
    
        for name, record in self.data.items():
            birthday_this_year = record.birthday.value.replace(year=today.year)
            
            if (birthday_this_year - today).days < 0:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= 7:
                birthday_this_year = self.__adjust_for_weekend(birthday_this_year)
                congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
                upcoming_birthdays.append({"name": name, "birthday": congratulation_date_str})
        return upcoming_birthdays
        
    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())