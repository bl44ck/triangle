# Function to categorize the triangle
def triangleType(a,b,c):
    """Categorize tree sides of a triangle into equilateral, unequal sided or isosceled.

    Args:
        a; int; Side a of the Triangle
        b; int; Side b of the Triangle
        c; int; Side c of the Triangle

    Returns:
        str; String of the category
    """

    if a == b == c:
        return "equilateral"
    elif a != b != c:
        return "unequal sided"
    else:
        return "isosceled"
