from collections import UserDict
from datetime import datetime
import signal
import pickle
import copy


class AddressBook(UserDict):

    def add_record(self, record):
        key = copy.deepcopy(record.name.value)
        value = copy.deepcopy(record)
        self.data[key] = value

    def iterator(self, n=1):
        br = 0  # for break for
        print(len(self.data))
        if n > len(self.data):
            n = len(self.data)
        for key in self.data.keys():
            if br < n:
                y = self.data.get(key)
                self.printdict(y)
                br += 1
            else:
                break

    def find(self, findword=""):
        for x in self.data.keys():
            if x.casefold() == findword.casefold():
                y = self.data.get(x)
                self.printdict(y)
            else:
                y = self.data.get(x)
                if findword.casefold() in y.phones[0].value.casefold():
                    self.printdict(y)
                elif findword.casefold() in y.birthday.value.casefold():
                    self.printdict(y)

    def save(self, path):
        # method for save data
        with open(path, "wb") as fh:
            pickle.dump(self.data, fh)

    def load(self, path):
        # method for load data
        try:
            with open(path, "rb") as fh:
                self.data = pickle.load(fh)
                return self.data
        except:
            print("Don't find any file, check Path and try again!")

    def printdict(self, y):
        if not (y.phones[0].value) and not (y.birthday.value):
            print("Record {}".format(y.name.value))
        elif (y.phones[0].value) and not (y.birthday.value):
            print("Record {}, phone number {}.".format(
                y.name.value, y.phones[0].value))
        elif not (y.phones[0].value) and y.birthday.value:
            print("Record {}, birthday {}, birthday coming through {} days.".format(
                y.name.value, y.birthday.value, y.days_to_birthday()))
        else:
            print("Record {}, phone number {}, birthday {}, birthday coming through {} days.".format(y.name.value, y.phones[0].value,
                                                                                                     y.birthday.value, y.days_to_birthday()))


class Field:
    pass


class Birthday(Field):
    field_birthday = "birthday"

    def __init__(self):
        self.__value = ""

    @ property
    def value(self):
        return self.__value

    @ value.setter
    def value(self, birthday):
        try:
            if datetime.strptime(birthday, "%d-%m-%Y"):
                self.__value = birthday
        except ValueError:
            print("This is the incorrect date string format. It should be DD-MM-YYYY")


class GracefulInterruptHandler(object):
    # this class copy from https://coderoad.ru/1112343/ to lazy create bicycle...

    def __init__(self, sig=signal.SIGINT):
        self.sig = sig

    def __enter__(self):

        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):

        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True

        return True


class Name(Field):
    field_name = "name"

    def __init__(self):
        self.__value = ""

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, name):
        self.__value = name


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = ""

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
        if self.birthday.value == None:
            return ""
        try:
            x = datetime.strptime(self.birthday.value, "%d-%m-%Y")
        except ValueError:
            return ""
        x = x.replace(year=a.year)
        if x < a:
            x = x.replace(year=(x.year+1))
        delta = x-a
        return str(delta.days)


class Phone(Field):
    field_phone = "phone"

    def __init__(self):
        self.__value = ""

    def format_phone_number(func):
        def inner(phone):
            phone1 = func(phone)
            if (12 <= len(phone1) <= 16):
                phone1 = ("+"+phone1)
                return phone1
            else:
                print(
                    "You enter wrong number, please try in this format: +11(111)111-11-11")
                return ""
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


if __name__ == "__main__":
    PATH = "SAVE.bin"
    with GracefulInterruptHandler() as h:
        ad = AddressBook()
        name = Name()
        phone = Phone()
        birth = Birthday()
        ad.load(PATH)
        ad.iterator(10)
        while True:

            name.value = input("Enter name: ")
            rec = Record(name)
            phone.value = input("Enter phone like +11(111)111-11-11: ")
            birth.value = input("Enter date like dd-mm-yyyy: ")
            rec.app_phone(phone)
            rec.add_birthday(birth)
            ad.add_record(rec)
            ad.save(PATH)
            y = input("Enter Name or Phone or Birthday to find contact: ")
            ad.find(y)

            x = input("any key to continue, 0 to exit")
            if x == "0":
                break

            if h.interrupted:
                # when close programm - save data in file Save
                ad.save(PATH)
                break
