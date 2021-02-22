from angle import angle
from isTriangle import isTriangle
from triangleType import triangleType

print("Welcome to our Triangle calculator, please enter sides a,b and c, e will exit the program")

while True:

    a = input("Enter side a:")
    if a.lower == e:
        break
    b = input("Enter side b:")
    c = input("Enter side c:")

    a = int(a)
    b = int(b)
    c = int(c)


    if isTriangle(a,b,c) == True:
        print("This is a valid triangle,")

        if angle(a,b,c) == 90:
            print("its rectangular")
        elif angle(a,b,c) > 90:
            print("its obtuse")
        else:
            print("its acute")

        if triangleType(a,b,c) == "equ":
            print("and equilateral.")
        elif triangleType(a,b,c) == "unequ":
            print("and unequal sided.")
        elif triangleType(a,b,c) == "iso":
            print("and isosceled.")

    else:
        print("This is no possible combination for a Triangle, try again.")
        continue
