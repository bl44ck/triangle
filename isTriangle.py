#code by Erion

def isTriangle(a,b,c):
    if (a + b > c) or (b + c > a) or (c + a > b):
        return True
    else:
        return False
