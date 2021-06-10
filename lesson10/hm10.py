from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Field:
    pass


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def app_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone):
        self.phones[phone] = phone


class Name(Field):
    field_name = "name"

    def __init__(self, name):
        self.value = name


class Phone(Field):
    field_phone = "phone"

    def __init__(self, phone):
        self.value = phone


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
