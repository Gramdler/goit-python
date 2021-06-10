from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, n=1):
        br = 0  # for break for
        if n > len(self.data):
            n = len(self.data)
        for key in self.data.keys():
            if br <= n:
                y = self.data.get(key)
                print("Record {}, phone number {}, birthday {}, birhday coming through {} days.".format(y.name.value, y.phones[0].value,
                                                                                                        y.birthday.value, y.days_to_birthday()))
            else:
                break


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

    def add_birthday(self, birthday):
        self.birthday = birthday

    def days_to_birthday(self):
        a = datetime.now()
        x = self.birthday.value
        x = x.replace(year=a.year)
        if x < a:
            x = x.replace(year=(x.year+1))
        delta = x-a
        return delta.days


class Name(Field):
    field_name = "name"

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, name):
        self.__value = name


class Phone(Field):
    field_phone = "phone"

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        self.__value = phone


class Birthday(Field):
    field_birthday = "birthday"

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birthday):
        self.__value = datetime.strptime(birthday, "%d-%m-%Y")


if __name__ == "__main__":

    name = Name()
    name.value = "Vasya"

    phone = Phone()
    phone.value = 333222444

    rec = Record(name)

    birh = Birthday()
    birh.value = str("28-06-1989")

    rec.app_phone(phone)
    rec.add_birthday(birh)

    print(str(rec.days_to_birthday()))

    print(rec.name.value)
    print(rec.phones[0].value)

    ad = AddressBook()
    ad.add_record(rec)

    print(ad.get("Vasya").name.value)
    print(ad.get("Vasya").phones[0].value)

    ad.iterator(2)
