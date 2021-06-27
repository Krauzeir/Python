import json

def carregar_dicionario():
    arquivo = open("pessoas.json", "r")
    dicionario = json.load(arquivo)
    
    return dicionario

def imprimir_dicionario(dicionario):
    print(dicionario)

def imprimir_pessoas(dicionario):
    pessoas = dicionario ["pessoas"]
    
    for pessoa in pessoas:
       print(pessoa)


if __name__ == '__main__':
    dicionario = carregar_dicionario()
    imprimir_dicionario(dicionario)
    imprimir_pessoas(dicionario)