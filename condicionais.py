def eh_igual (a,b):
    if a == b:
        return True
    else:
        return False

def eh_igual_curto(a, b):
    return (a == b)

def pelo_menos_dois_igauis(a, b, c):
    if a == b:
        return True
    elif a == c:
        return True
    elif b == c:
        return True
    else:
        return False  


if __name__ == '__main__':
    if eh_igual(2,2):
        print("iguais")
    else:
        print("diferentes")
        
    if eh_igual(3,2):
        print("iguais")
    else:
        print("diferentes")
    
    if eh_igual_curto(2,2):
        print("iguais")
    else:
        print("diferentes")
        
    if pelo_menos_dois_igauis(2,3,2):
        print("Existem 2 iguais")
    else:
        print("Todos são diferentes")
        
    if pelo_menos_dois_igauis(2,3,4):
        print("Existem 2 iguais")
    else:
        print("Todos são diferentes")
        
