import colored

def somar(a, b):
    c = a + b
    
    return c

def mostrar_resultado(resultado):
    print(colored.fg("white"), colored.bg("red"), "resultado: ", resultado, colored.attr("reset"))
    
if __name__ == '__main__':
    resultado = somar (1,2)
    mostrar_resultado(resultado)
    