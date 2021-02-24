from angle import angle
from isTriangle import isTriangle
from triangleType import triangleType

print("Welcome to our Triangle calculator, please enter sides a, b and c, 0 (Zero)" +
    " will exit the program.")

while True:

    a = int(input("Enter side a: "))
    if a == 0:
        break
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))


    if isTriangle(a,b,c) == True:
        print("This is a valid triangle,")

        if angle(a,b,c) == 90:
            print("its rectangular")
        elif angle(a,b,c) > 90:
            print("its obtuse")
        else:
            print("its acute")

        if triangleType(a,b,c) == 0 :
            print("and equilateral.")
        elif triangleType(a,b,c) == 2:
            print("and unequal sided.")
        elif triangleType(a,b,c) == 1:
            print("and isosceled.")

    else:
        print("This is no possible combination for a Triangle, try again.")
        continue
