# Angle-Calculation

# Import
import numpy

def angle(a, b, c):
    ''' Angle calculation with cosine-theorem using the three sides of a triangle.

    α = arccos( (b² + c² - a²) / 2bc )
    β = arccos( (a² + c² - b²) / 2ac )
    γ = arccos( (a² + b² - c²) / 2ab )

    Quelle: https://rechneronline.de/pi/dreieck.php

    Arguments:
        a int -- side a
        b int -- side b
        c int -- side c

    Returns:
        float, float, float -- Angles α, β, γ

    '''
    global angle_c
    # Calculate arc cosine according to above formulas
    arccos_c = numpy.arccos((a*a + b*b - c*c) / (2 * a * b))

    # Arc cosine is in radian (radian measure) and must be transformed
    # into degrees
    angle_c = numpy.rad2deg(arccos_c)

    return angle_c
