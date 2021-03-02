#
# Dreiecksberechnung
#

# Authoren: S. Camathias
#           O. Eggenberger
#           F. Fortin
#           E. Shatri

# Version: 1.0
# Abgabe am 04.03.2021 bei P. Kessler
# Bewertete Abgabe im Fach: 'Grundlagen Programmieren'

# Folgende im Unterricht gelernten "Sachen" wurden hier eingebaut:
# (Oder zumindest versucht einzubauen. Es kann dadurch zu unnötigen Funktionen oder
# speziellen Lösungen kommen.)
#   - Funktionen, inklusive Docstrings
#   - Rückgabewerte als Boolean (Gültig) und String (Winkel und Seiten)
#   - Listen
#   - Tupel
#   - Dictionarys
#   - Endlosschleife
#   - if/else-Abfragen, while Schleife, for Schleife
#   - Break und Continue Bedingungen
#   - Exceptionhandling
#   - Print Befehle mit Zeilenabständen, Einrückungen, Überschreiben der Zeile und Kombinationen mit Listeneinträgen
#   - Vermeidung von repetitivem Code
#   - Es wurde versucht den Code optimal zu schreiben, um unnötige Hardwarebelastung zu vermeiden
#   - Und wie man sieht haben wir auch Kommentare eingebaut

# Funktionen importieren, auch aus anderen Dateien.
from Gültig import gueltig_dr
from Winkel import winkel_gamma
from Seitenauswertung import seiten_auswertung
import time
import random

# Variabel, unveränderbare Listen (Tupel)
# Dient der Auswertung des Winkel.
winkel = ('rechtwinkliges', 'spitzwinkliges', 'stumpfwinkliges')

# Dictionary
# Dient der Auswertung der Seiten
seiten = {
'gl' : 'gleichseitiges',
'un' : 'ungleichseitiges',
'gs' : 'gleichschenkliges'
}

# Anfang des Hauptprogrammes
# Endlosschleife bis break Bedingung erfüllt ist.
while True:

    # Optische Einleitung in das Programm
    print('----------------------------------------------------\n')

    # Variablen, veränderbare Liste, wird verwendet um die Ausgabe zu machen.
    # Die Platzierung wurde absichtlich innerhalb der Schlaufe gewählt, damit bei
    # jedem Durchlauf die Liste geleert wird.
    ausgabe = []

    # Start Exceptionhandling
    try:
        # Aufforderung zur Eingabe
        # Mit Bekanntgabe der Abbrucheingabe
        print('Bitte gib die Längen a, b und c an. (in Ganzzahlen)' +
            '\nMit "0" kannst du das Programm verlassen.')
        # Direkte Integer Eingabe damit keine Umwandlung gemacht werden muss
        # und der Code kleiner bleibt.
        a = int(input('Länge der Seite a: '))
        # Abbruchbedingung, bei 0 (Null) wird das Programm verlassen
        if a == 0:
            break
        # Wie bei a.
        b = int(input('Länge der Seite b: '))
        if b == 0:
            break
        # Wie bei a
        c = int(input('Länge der Seite c: '))
        if c == 0:
            break

    # Exceptionhandling
    # Continue wenn Eingabe ungültig
    except ValueError:
        print('Bitte gib eine Ganzzahl ein.\n')
        continue

    # Gültig oder Ungültig, bei Ungültig (False) geht es wieder in die
    # erste While-Schleife (Endlosschlaufe).
    if gueltig_dr(a, b, c) == False:
        print('Diese Seitenlängen ergeben kein Dreieck.\n')
        continue

    else:

        # Zur Optimierung wird der Winkel hier einmal ausgerechnet und
        # danach nur noch verglichen.
        # Versuch der Rechenleistungsoptimierung
        winkel_vergleich = winkel_gamma(a, b, c)

        # Es wird der Rückgabewert genommen und danach das entsprechende Element
        # aus dem Tupel winkel in die Liste ausgabe gepackt.
        if winkel_vergleich == 90.0:
            ausgabe.append(winkel[0])

        elif winkel_vergleich < 90.0:
            ausgabe.append(winkel[1])

        else:
            ausgabe.append(winkel[2])

        # Seitenverhältnis wird verglichen.
        # Rückgabe eines Strings.
        seiten_vergleichen = seiten_auswertung(a, b, c)

        # Ausgabe mittels Satzbausteinen,dem Strings aus der Liste Ausgabe
        # und dem entsprechenden Eintrag im Dictionary.
        # Ausgabe absichtlich so gewählt, damit im Programm mit Listen, Tupel und
        # Dictionarys gearbeitet worden ist.
        print('Du hast ein ' + ausgabe[0] + ', ' + seiten[seiten_vergleichen] +
            ' Dreieck.\n')

# Ausgabe wenn das Programm beendet wurde.
# Inklusive dem unten angehängten Countdown.
print('\nDanke das du mit unserem Programm gearbeitet hast.\n\n' +
'----------------------------------------------------\n')

# Timer beim Beenden des Programmes.
# Text ist standardisiert, die Countdown-Zeile überschreibt sich nach jeder Iteration.
for i in range(1, 6):
    print('\tDieses Programm wird geschlossen in 00:0' + str(5 - i) + ' Sekunden!', end=('\r'))
    time.sleep(1)

# Kleines Easteregg das nicht ersichtlich ist, wenn das Programm in der Shell geöffnet wird.
# Etwas auflockerndes zum Schluss.
# Das Programm macht immer noch was es soll, kein Schadcode wurde eingebaut!
import random

easteregg = (
'\tHasta la Vista Baby!                                               ',
'\tI will be back!                                                    ',
'\tHere comes the Boom!                                               ',
'\tSee you later Aligator!                                            ',
'\tWe will never be Slaves!                                           ',
'\tNobody is Perfect!                                                 ',
'\tGood Evening, Vietnam!                                             ',
'\tWenn du denkst du hast einen Dummen vor dir, bist du an der rirchtigen Adresse!',
'\tWir lassen Bier und Würstchen entscheiden!                         ',
)

r = random.randint(0, 9)
print(easteregg[r])