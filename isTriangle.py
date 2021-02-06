#code by Erion

#a = int(input ("Bitte seite a eingeben:"))
#b = int(input ("Bitte seite b eingeben:"))
#c = int(input ("Bitte seite c eingeben:"))

def isTriangle(a,b,c):
    if (a + b <= c) or (b + c <= a) or (c + a <= b):
        False
    else:
        True
