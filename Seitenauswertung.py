#
# Seitenauswertung
#

# Die Funktion vergleicht die Seiten und gibt einen definierten Wert zurück.
# Anhand dieses Wertes wird dann aus dem Dictionary seiten das entsprechende Element
# in Ausgabe angezeigt.

# Um die Hardware zu schonen haben wir den Vergleich a == b und b == c weggelassen.
# Da hier zwei Anforderungen gleichzeitig abgeklärt werden müssen, wird unserer Meinung
# nach mehr Hardwarepower benötigt.

def seiten_auswertung(a, b, c):
    ''' Auswertung des Seitenverhältnis eines Dreiecks.

    Argumente:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Rückgabewerte:
        str -- Seitenverhältnis
    '''
    if a == b == c:
        return 'gl'

    elif a != b != c:
        return 'un'

    else:
        return 'gs'