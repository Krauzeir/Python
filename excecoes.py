def dividir(a, b):
    if (b == 0):
        return 0
    else:
        return a/b

if __name__ == '__main__':
    try:
        divisao = dividir(3,0)
        print("resultado: ", divisao)
    except ZeroDivisionError:
        print("Não se pode dividir um número por zero!")
    
