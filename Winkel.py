#
# Winkel Berechnung
#

# Die Funktion rechnet den Arccos aus, wandelt den Wert von Bogenmass in Grad um
# und gibt einen definierten Wert zurück.
# Anhand dieses Wertes wird dann aus dem Tupel seiten das entsprechende Element
# in die Liste auswertung gepackt.

# Wir haben auf die Winkel Alpha und Beta verzichtet, da bei der Aufgabenstellung
# die Seite C als Hypothenuse definiert wurde.
# Durch das Weglassen der Berechnung von Alpha und Beta wird eine minimierung der
# Hardwareleistung angestrebt.
def winkel_gamma(a, b, c):
    ''' Winkel Berechnung mit Kosinussatz anhand der drei Seiten eines Dreieckes

    γ = arccos( (a² + b² - c²) / 2ab )

    Quelle: https://rechneronline.de/pi/dreieck.php

    Argumente:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Rückgabewert:
        float -- des Winkel γ

    '''
    # Import um die Berechnungen zu machen.
    # Wir haben uns für Math entschieden, da Numpy nicht Standardmässig bei
    # Python heruntergeladen wird. Der Code soll aber egal ob mit oder ohne Anaconda
    # oder einer zusätzlichen Installation laufen.
    import math

    # Arkuscosinus berechnen gem. obiger Formeln
    arccos_c = math.acos((a*a + b*b - c*c) / (2 * a * b))

    # Arkuscosinus umwandeln in degree (Gradmass)
    winkel = math.degrees(arccos_c)

    return winkel