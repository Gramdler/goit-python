### Second homework to lesson 1 in goit ###

print("Hello User!\nThis script for solving quadratic equation (ax^2 + bx + c = 0), please enter some parameters: ")

a = float(input("Please enter a: "))
b = float(input("Please enter b: "))
c = float(input("Please enter c: "))

d = float(b * b - 4 * a * c)
if d > 0:
    x1 = round((-b+d**0.5)/2*a, 1)
    x2 = round((-b-d**0.5)/2*a, 1)
    print(f" x1 = {str(x1)};", end="")
    print(f" x2 = {str(x2)}")
elif d == 0:
    x = round((-b+d**0.5)/2*a, 1)
    print(f" x = {str(x)};")
else:
    print("This quadratic equation doesn't have solution.")
