### Task 3 The simple calculator in console (+,-,/,*)###
# User enter operands and operators and take result when entering "="
# If the User enters the wrong data program send a  message about it and ask to enter the right data.
import re
print("Welcome to console calculater!\nPlease enter step by step operators and operands.")
print('When you want to take result enter "="\nWhen you want quit enter "q"')

operations = ["+", "-", "/", "*"]
operation = []
operand1 = []
operand2 = []
checker = 0
flag = True


def check(str):  # to economy time to write code.
    try:
        float(str)
        return str.strip()
    except ValueError:
        if len(str.strip()) == 1:
            if str in operations:
                return str.strip()
            elif str == '=':
                return str.strip()
            elif str.lower() == "q":
                return str.strip()
        str = "wrong data"
        return str


def equty(operand1=[], operation=[], operand2=[]):  # enter list return list.
    s = 0
    if len(operand1) == len(operand2) and len(operand1) == len(operation):
        while operation:
            temp = operation.pop()
            if temp == "+":
                s = s + float(operand1.pop()) + float(operand2.pop())
                print(operation)

            elif temp == "-":
                s = s + float(operand1.pop()) - float(operand2.pop())
                print(operation)

            elif temp == "*":
                s = s + float(operand1.pop()) * float(operand2.pop())
                print(operation)

            elif temp == "/":
                try:
                    s = s + float(operand1.pop()) / float(operand2.pop())
                    print(operation)

                except ZeroDivisionError:
                    print("You delete on zero! Try again!")
            else:
                print("Wrong action")
        return s
    elif len(operand1) > len(operand2):
        print("operand1 > operand2")
    elif len(operand1) < len(operand2):
        print("operand1 < operand2")
    elif len(operand1) < len(operation):
        print("operand1 < operation")
    elif len(operand1) > len(operation):
        print("operand1 > operation")
        s = operand1.pop()
        return s
    elif len(operand2) < len(operation):
        print("operand2 < operation")
    elif len(operand2) > len(operation):
        print("operand2 > operation")
    else:
        return 0


while flag:
    while checker == 0:
        a = check(input("Please enter operand: "))
        if a == "wrong data":
            print("You enter wrong data, please try again!")
        elif a in operations:
            print("You enter operations, this mistake, try again!")
        elif a.isdigit and a != "=":
            operand1.append(a)
            print(operand1)
            checker = 1
        elif a.lower() == "q":
            flag = False
            break
        elif a == '=':
            a = equty(operand1, operation, operand2)
            print(f"Your result:{a}")
            flag = False
            break
    while checker == 1:
        a = check(input("Please enter operarion: "))
        if a == "wrong data":
            print("You enter wrong data, please try again!")
        elif a in operations:
            operation.append(a)
            print(operation)
            checker = 2
        elif a.lower() == "q":
            flag = False
            break
        elif a == '=':
            try:
                if operation[(len(operation) - 1)] == "/":
                    operand2.append("1")
                else:
                    operand2.append("0")
            except IndexError:
                operand2.append(
                    "0") if "/" not in operation else operand2.append("1")
            a = equty(operand1, operation, operand2)
            print(f"Your result:{a}")
            break
            flag = False
        elif a.isdigit and a not in operations and a != "=":
            print("You enter operand, this mistake, try again!")
    while checker == 2:
        a = check(input("Please enter operand 2: "))
        if a == "wrong data":
            print("You enter wrong data, please try again!")
        elif a in operations:
            print("You enter operations, this mistake, try again!")
        elif a.isdigit and a != "=":
            operand2.append(a)
            print(operand2)
            checker = 0
        elif a.lower() == "q":
            flag = False
            break
        elif a == '=':
            if operation[(len(operation) - 1)] == "/":
                operand2.append("1")
            else:
                operand2.append("0")
            a = equty(operand1, operation, operand2)
            print(f"Your result:{a}")
            flag = False
            break
