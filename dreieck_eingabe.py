

a = int(input ("Bitte seite a eingeben:"))
b = int(input ("Bitte seite b eingeben:"))
c = int(input ("Bitte seite c eingeben:"))



if (a + b <= c) or (b + c <= a) or (c + a <= b):
    print("Eingabe nich möglich")

else:
    True


