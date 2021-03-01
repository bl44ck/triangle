# Import
import math

def angle(a, b, c):
    """Categorizes angles of 3 sides into rectangular,obtuse and acute.

    Args:
        a; int; Side a of the Triangle
        b; int; Side b of the Triangle
        c; int; Side c of the Triangle

    Returns:
        str; String of the category
    """

    #Calculate cos
    cos = ((a*a + b*b - c*c) / (2 * a * b))

    if cos > 1.0 or cos < -1.0:
        return "Failed, wrong cos"

    # Calculate Arccos
    arccos_c = math.acos(cos)

    # Arc cosine is in radian and must be transformed into degrees
    angle_c = math.degrees(arccos_c)

    if angle_c == 90:
        return "rectangular"
    elif angle_c > 90:
        return "obtuse"
    else:
        return "acute"