# Authoren: S. Camathias
#           O. Eggenberger
#           F. Fortin
#           E. Shatri

#import
from angle import angle
from isTriangle import isTriangle
from triangleType import triangleType
import time
import random

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


def endProgram(waitTime):
    """Ends the program with a feedback.

    Args:
        waitTime ; int ; Set the countdown to stop the program, 0 results in imidiate exit.

    Return:
        no return, just ends the program.
    """
    goodbye = ["Hasta la vista, baby!","I'll be back!","See you later aligator!"]
    r = random.randint(0,2)
    print(goodbye[r])
    time.sleep(waitTime)
    exit()

while True:

    print("----------------------------------------------")
    print("Please enter sides a, b and c, 0 (Zero)" +
    " will exit the program. Only Integers are allowed.")
    print("----------------------------------------------\n")


#input
    try:

        a = int(input('Side a:\n'))
        if a == 0:
            endProgram(1)

        b = int(input('Side b:\n'))
        if b == 0:
            endProgram(1)

        c = int(input('Side c:\n'))
        if c == 0:
            endProgram(1)

    except ValueError:
        print('Integers only. Sorry :(\n')
        continue

#output
    output()

    continue
