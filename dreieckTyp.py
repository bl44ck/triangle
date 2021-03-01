# Function to categorize the triangle
def dreieckTyp(a,b,c):
    """Kategorisiert drei Seiten eines Dreiecks in gleichseitig, ungleichseitig oder gleichschenklig.

    Args:
        a; int; Seite a des Dreiecks
        b; int; Seite b des Dreiecks
        c; int; Seite c des Dreiecks

    Returns:
        str; String der Kategorie
    """

    if a == b and b == c:
        return "gleichseitiges"
    elif a == b or a == c or b ==c:
        return "ungleichseitiges"
    else:
        return "gleichschenkliges"