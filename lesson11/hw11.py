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
                if not (y.phones[br].value) and not (y.birthday.value):
                    print("Record {}".format(y.name.value))
                elif (y.phones[br].value) and not (y.birthday.value):
                    print("Record {}, phone number {}.".format(
                        y.name.value, y.phones[br].value))
                elif not (y.phones[br].value) and y.birthday.value:
                    print("Record {}, birthday {}, birhday coming through {} days.".format(
                        y.name.value, y.birthday.value, y.days_to_birthday()))
                else:
                    print("Record {}, phone number {}, birthday {}, birhday coming through {} days.".format(y.name.value, y.phones[br].value,
                                                                                                            y.birthday.value, y.days_to_birthday()))
                br += 1
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
        if x == None:
            return None
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

    def format_phone_number(func):
        def inner(phone):
            phone1 = func(phone)
            if (12 <= len(phone1) <= 16):
                phone1 = ("+"+phone1)
                return phone1
            else:
                print(
                    "You enter wrong number, please try in this format: +11(111)111-11-11")
                return None
        return inner

    @ format_phone_number
    def sanitize_phone_number(phone):
        new_phone = (
            phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone

    @ property
    def value(self):
        return self.__value

    @ value.setter
    def value(self, phone, x=sanitize_phone_number):
        self.__value = x(phone)


class Birthday(Field):
    field_birthday = "birthday"

    def __init__(self):
        self.__value = None

    @ property
    def value(self):
        return self.__value

    @ value.setter
    def value(self, birthday):
        try:
            self.__value = datetime.strptime(birthday, "%d-%m-%Y")
            print("This is the correct date string format.")
        except ValueError:
            print("This is the incorrect date string format. It should be DD-MM-YYYY")


if __name__ == "__main__":

    name = Name()
    name.value = "Vasya"

    phone = Phone()
    phone.value = "380985202222"

    rec = Record(name)

    birh = Birthday()
    birh.value = str("28-06-1989")

    rec.app_phone(phone)
    rec.add_birthday(birh)

    ad = AddressBook()
    ad.add_record(rec)

    ad.iterator(2)
