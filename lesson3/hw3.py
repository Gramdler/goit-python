### Task 3 The simple calculator in console (+,-,/,*)###
# User enter operands and operators and take result when entering "="
# If the User enters the wrong data program send a  message about it and ask to enter the right data.

print("Welcome to console calculater!\nPlease enter step by step operands and operators.")
print('When you want to take result enter "="\nWhen you want quit enter "q"')
print("If you don't enter first operator and second operand = you take back firs operand")
print("If you don't enter next operator = you lost next first operand, and take result without it")
print("This calculator doesn't support - ().")

operations = ["+", "-", "/", "*"]
operation = []
operand1 = []
operand2 = []
checker = 0
flag = True


def check(str):  # to economy time to write code.
    ### Enter string, check it to right rules, end retunr sring ###
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


def equty(operand1=[], operation=[], operand2=[]):
    ### Enter lists: first operands, opeartions, second operands, and return float number###
    s = 0
    if len(operand1) == len(operand2) and len(operand1) == len(operation):
        while operation:
            temp = operation.pop()
            if temp == "+":
                s = s + float(operand1.pop()) + float(operand2.pop())
                # print(operation)
            elif temp == "-":
                s = s + float(operand1.pop()) - float(operand2.pop())
                # print(operation)
            elif temp == "*":
                s = s + float(operand1.pop()) * float(operand2.pop())
                # print(operation)
            elif temp == "/":
                try:
                    s = s + float(operand1.pop()) / float(operand2.pop())
                    # print(operation)
                except ZeroDivisionError:
                    print("You divide on zero! Try again!")
            else:
                print("Wrong action")
        return s
    elif len(operand1) > len(operand2):
        #print("operand1 > operand2")
        s = operand1.pop()
        return s
    elif len(operand1) > len(operation):
        #print("operand1 > operation")
        s = operand1.pop()
        return s
    else:
        return 0


# future options, if we delete flag = False, were a == "=", we get working mini-program.
while flag:
    while checker == 0:  # Take first operand.
        a = check(input("Please enter first operand or = : "))
        if a == "wrong data":
            print("You entered wrong data, please try again!")
        elif a in operations:
            print("You entered type of operation, this mistake, try again!")
        elif a != "=" and a.lower() != 'q':
            operand1.append(a)
            # print(operand1)  # this and next code to quickly check code.
            checker = 1
        elif a.lower() == "q":
            flag = False
            break
        elif a == '=':
            a = equty(operand1, operation, operand2)
            print(f"Your result: {a}")
            flag = False
            break
    while checker == 1:  # Take operation.
        a = check(input("Please enter type of operarion or = : "))
        if a == "wrong data":
            print("You entered wrong data, please try again!")
        elif a in operations:
            operation.append(a)
            # print(operation)
            checker = 2
        elif a.lower() == "q":
            flag = False
            break
        elif a == '=':
            # Check if operand1 > operaor , end we have more operands1
            if len(operand1) > len(operation):
                if len(operand1) > 1:
                    operand1.pop()
            else:
                try:
                    if operation[(len(operation) - 1)] == "/":
                        operand2.append("1")
                    else:
                        operand2.append("0")
                except IndexError:
                    operand2.append(
                        "0") if "/" not in operation else operand2.append("1")
            a = equty(operand1, operation, operand2)
            print(f"Your result: {a}")
            flag = False
            break
        elif a not in operations and a != "=":
            print("You entered operand, this mistake, try again!")
    while checker == 2:  # Take second operand
        a = check(input("Please enter second operand or = : "))
        if a == "wrong data":
            print("You entered wrong data, please try again!")
        elif a in operations:
            print("You entered type of operation, this mistake, try again!")
        elif a.lower() != "q" and a != "=":
            operand2.append(a)
            # print(operand2)
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
            print(f"Your result: {a}")
            flag = False
            break
