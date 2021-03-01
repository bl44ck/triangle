def isTriangle(a,b,c):
    """Check if three integers are a possible triangle

    Args:
        a; int; Side a of the Triangle
        b; int; Side b of the Triangle
        c; int; Side c of the Triangle

    Returns:
        bool; true if valid, false if invalid
    """
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False
