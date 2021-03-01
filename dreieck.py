#import
from winkel import winkel
from istDreieck import istDreieck
from dreieckTyp import dreieckTyp

def ausgabe():
    """Schreibt den Ausgabetext in die Konsole

    Args:
        keine Argumente

    Returns:
        keine, Schreibt Text
    """
    winkelAusgabe = winkel(a,b,c)
    TypAusgabe = dreieckTyp(a,b,c)
    if istDreieck(a,b,c) == True:
        print(f"Das ist ein gültiges, {winkelAusgabe} und {TypAusgabe} Dreieck!")
    else:
        print("Das ist kein gültiges Dreieck, überprüfe deine Eingabe!")

while True:

    print("Bitte gib die Seiten a, b und c an, 0 (Null)" +
    " beendet das Programm. Nur Integer benutzen.")

#Eingabe
    a = int(input("Seite a: "))
    if a == 0:
        break
    b = int(input("Seite b: "))
    c = int(input("Seite c: "))

#Ausgabe
    ausgabe()
    
    continue