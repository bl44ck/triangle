# Import
import math

def winkel(a, b, c):
    """Kategorisiert die Winkel von 3 Seiten in rechteckig, stumpfwinklig und spitzwinklig.

    Args:
        a; int; Seite a des Dreiecks
        b; int; Seite b des Dreiecks
        c; int; Seite c des Dreiecks

    Returns:
        str; String der Kategorie
    """

    #Berechne cos
    cos = ((a*a + b*b - c*c) / (2 * a * b))

    if cos > 1.0 or cos < -1.0:
        return "Fehlgeschlagen, falscher cos"

    # Berechne Arccos
    arccos_c = math.acos(cos)

    # Acos ist in RAD und muss in DEG konvertiert werden
    winkel_c = math.degrees(arccos_c)

    if winkel_c == 90:
        return "rrechteckiges"
    elif winkel_c > 90:
        return "stumpfwinkliges"
    else:
        return "spitzwinkliges"