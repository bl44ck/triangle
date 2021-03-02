#
# Abklärung Gültig / Ungültig
#

# Wertet durch vergleichen aus, ob die Eingaben ein Gültiges Dreieck ergeben.
# Rückgabewert ist gueltig.

# Falls es ein gültiges Dreieck ist,
# wird gueltig auf True und bei einer ungültigen Eingabe auf False gesetzt.
def gueltig_dr(a, b, c):
    ''' Klärung ob die Eingaben ein gültiges Dreieck ergeben.

    Argumente:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Rückgabewert:
        bool -- Gültigkeit
    '''
    gueltig = False

    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        gueltig = True

    # Es wird keine zweite Auswertung gemacht, da es nur 2 Zustände gibt.
    # Der Wert False ist ja schon gesetzt.
    # Optimierung der Hardwareleistung.
    return gueltig