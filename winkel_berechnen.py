# Dreiecksbestimmung

# Importe
import numpy

# Funktionen
def winkel_dr(a, b, c):
    ''' Winkel Berechnung mit Kosinussatz anhand der drei Seiten eines Dreieckes

    α = arccos( (b² + c² - a²) / 2bc )
    β = arccos( (a² + c² - b²) / 2ac )
    γ = arccos( (a² + b² - c²) / 2ab )

    Quelle: https://rechneronline.de/pi/dreieck.php

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        float, float, float -- die Winkel α, β, γ

    '''
    global winkel_c
    # Arkuscosinus berechnen gem. obiger Formeln
    arccos_c = numpy.arccos((a*a + b*b - c*c) / (2 * a * b))

    # Arkuscosinus ist in radiant (Bogenmass) und muss umgewandelt
    # werden in degree (Gradmass)
    winkel_c = numpy.rad2deg(arccos_c)

    return winkel_c