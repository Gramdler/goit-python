from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    count = 0

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self):
        pass


class Field:
    pass


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def app_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone):
        self.phones[phone] = phone

    def days_to_birthday(self):
        pass


class Name(Field):
    field_name = "name"

    def __init__(self, name):
        self.value = name


class Phone(Field):
    field_phone = "phone"

    def __init__(self, phone):
        self.value = phone


class Birthday(Field):
    field_birthday = "birthday"

    def __init__(self, birthday):
        self.value = birthday


if __name__ == "__main__":

    name = Name("Vasya")
    phone = Phone(333222444)
    rec = Record(name)
    rec.app_phone(phone)

    print(rec.name.value)
    print(rec.phones[0].value)

    ad = AddressBook()
    ad.add_record(rec)

    print(ad.get("Vasya").name.value)
    print(ad.get("Vasya").phones[0].value)
