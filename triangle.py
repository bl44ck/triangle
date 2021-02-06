print("Welcome to our Triangle calculator, please enter sides a,b and c, e will exit the program")

a = input("Enter side a:")
b = input("Enter side b:")
c = input("Enter side c:")

if a == "e":
    exit
else:
    break

if isTriangle(a,b,c) == True:
    print("This is a valid triangle,")
else:
    print("This is no possible combination for a Triangle, try again.")

if angle(a,b,c) == 90:
    print("its rectangular")
elif angle(a,b,c) > 90:
    print("its acute")
else:
    print("its obstuse")

if triangleType(a,b,c) == "equ":
    print("and equilateral.")
elif triangleType(a,b,c) == "rgt":
    print("and right angeled.")
elif triangleType(a,b,c) == "iso":
    print("and isosceled.")