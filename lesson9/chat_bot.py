# task 9
import re
import random

voca_phone = {}
name = number = ""


def add(s=''):
    name, number = sep_text(s)
    voca_phone[name] = number
    return "Contact had been added."


def change(s=''):
    name, number = sep_text(s)
    try:
        voca_phone[name] = number
    except KeyError:
        print("Wrong name, please add name and phone first")
    return "Contact had been changed."


def phone(s=''):
    name, number = sep_text(s)
    phone_number = ""
    try:
        phone_number = voca_phone[number]
    except KeyError:
        print("Wrong name, please add name and phone first")
    return phone_number


def show_all(*args):
    list_of_contacts = ""
    for key, value in voca_phone.items():
        list_of_contacts += f"Name: {key}\n Number: {value} \n"
    return list_of_contacts


def good_bye(*args):
    print("Good bye!")
    return "0"


def hello(*args):
    answer = random.choice(
        ['How can I help you?', 'Please enter name and phone number'])
    return answer


def help1(*args):
    s = 'Use add(Name Phone_number) - to add contact\n Use change(Name Phone_number) - to change number\n Use phone(Name) - to get phone number\n Use show_all - show all contacts, \n Use good_bye, exit, close, . - go out'
    return s


def sentece_writer(x=[]):
    sentence = ""
    for word in x:
        sentence += str(word)+" "
    sentence = sentence.strip()
    return sentence


def sep_text(x=''):
    name = ""
    number = ""
    t = x.split(" ")
    if t:
        for word in t[1:-1]:
            name += word + " "
        number = t[-1]
    name = name.strip()
    return name, number


def get_intent(text):
    for intent in BOT_CONFIG['intents']:
        for example in BOT_CONFIG['intents'][intent]['examples']:
            if example == text:
                return intent


def handler(text):
    list_text = re.findall(r"\w+|[\w+][\w+]|[\w+][\w+][\w+][\d{7,9}]", text)
    sentence = sentece_writer(list_text)
    a = list_text[0]
    a = a.casefold()
    intent = get_intent(a)  # 1. Попытаться понять намерение

    if intent is not None:       # 2. Ответить в соответствии намеренения
        x = random.choice(BOT_CONFIG['intents']
                          [intent]['responses'])(sentence)
    else:        # 3. Если не получилось ответить заглушкой
        x = random.choice(BOT_CONFIG['default_answers'])
    return x


def main():
    text = input("Give me name and phone please: ")
    x = handler(text)
    print(x)
    return x


BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['hello', 'hi', 'hi!', 'good day!'],
            'responses': [hello]
        },
        'bye': {
            'examples': ['good bye', 'close', 'exit', '.'],
            'responses': [good_bye]
        },
        'add': {
            'examples': ['add'],
            'responses': [add]
        },
        'change': {
            'examples': ['change'],
            'responses': [change]
        },
        'phone': {
            'examples': ['phone'],
            'responses': [phone]
        },
        'show_all': {
            'examples': ['show_all'],
            'responses': [show_all]
        },
        'help': {
            'examples': ['help'],
            'responses': [help1]
        }
    },
    'default_answers': ['You enter wrong data, give me name and phone please.']
}

if __name__ == "__main__":
    while True:
        x = main()
        if x == "0":
            break
