# Input
print('Bitte gib die Längen a, b und c an. (in Ganzzahlen)' +
    '\nMit "Ende" kannst du das Programm verlassen.')
a = input('Länge der Seite a: ')

# Abbruchbedingung
if a.lower() == 'ende':
    break

b = input('Länge der Seite b: ')
c = input('Länge der Seite c: ')


# Integer Umwandlung
a = int(a)
b = int(b)
c = int(c)