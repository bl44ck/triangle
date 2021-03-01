#import
from angle import angle
from isTriangle import isTriangle
from triangleType import triangleType

def output():
    """Outputs the variables in one string.

    Args:
        no args

    Returns:
        no return, prints the text as seen below.
    """
    angle_output = angle(a,b,c)
    type_output = triangleType(a,b,c)
    if isTriangle(a,b,c) == True:
        print(f"This is a valid, {angle_output} and {type_output} triangle!")
    else:
        print("This is no valid triangle, please check your inputs!")

while True:

    print("Please enter sides a, b and c, 0 (Zero)" +
    " will exit the program. Only Integers are allowed.")

#input
    a = int(input("Enter side a: "))
    if a == 0:
        break
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))

#output
    output()
    
    continue