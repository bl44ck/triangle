def istDreieck(a,b,c):
    """Überprüft ob drei Integer ein Dreieck bilden können

    Args:
        a; int; Seite a des Dreiecks
        b; int; Seite b des Dreiecks
        c; int; Seite c des Dreiecks

    Returns:
        bool; True wenn gültig, False wenn ungültig
    """
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False
