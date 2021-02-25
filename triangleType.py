#Triangletype-definition by Oliver

def triangleType(a,b,c):

    if a == b and b == c:
        return 0
    elif a == b or a == c or b ==c:
        return 1
    else:
        return 2
