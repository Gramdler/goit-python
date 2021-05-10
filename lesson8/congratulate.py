# functuion to print list of birthdays in the next week.
from datetime import datetime
from datetime import timedelta


def printfun(li=[]):
    s = ""
    if li:
        for l in li:
            s += f'{l}, '
        s = s.removesuffix(", ")
        print(s, end="")
        print()
    else:
        pass


def congratulate(users={}):
    counter = 0
    current_date = datetime.now()
    Mon = []
    Tue = []
    Wed = []
    Thu = []
    Fri = []
    for key, value in users.items():
        date = datetime.strptime(value, "%d-%m-%Y")
        date = date.replace(year=current_date.year)
        x = int(current_date.weekday())
        while x < 5:
            x += 1
        left_week = (current_date + timedelta(days=x-2))
        next_week = (current_date + timedelta(days=x+5))
        if left_week < date < next_week:
            if datetime.strftime(date, '%w') == "2":
                Tue.append(key)
            elif datetime.strftime(date, '%w') == "3":
                Wed.append(key)
            elif datetime.strftime(date, '%w') == "4":
                Thu.append(key)
            elif datetime.strftime(date, '%w') == "5":
                Fri.append(key)
            else:
                Mon.append(key)
    if Mon:
        print("Monday: ", end="")
        printfun(Mon)
    if Tue:
        print("Tuesday: ", end="")
        printfun(Tue)
    if Wed:
        print("Wednesday: ", end="")
        printfun(Wed)
    if Thu:
        print("Thursday: ", end="")
        printfun(Thu)
    if Fri:
        print("Friday: ", end="")
        printfun(Fri)


if __name__ == "__main__":

    USERS = {
        "Bill": "16-05-1980",
        "Jill": "17-05-1972",
        "Kim": "21-05-1973",
        "Jan": "21-05-1998"
    }

    congratulate(USERS)
