def criar_dicionario():
    dicionario = {
        "nome" : "João da Silva",
        "idade" : 25,
        "profissao" : "medico"
    }
    
    return dicionario
    
def imprimir_dicionario(dicionario):
    print(dicionario)
    
def imprimir_nome(dicionario):
    print("nome", dicionario["nome"])    
    
def imprimir_idade(dicionario):
    print("idade", dicionario["idade"])    
    
def imprimir_profissao(dicionario):
    print("profissao", dicionario["profissao"])    

if __name__ == '__main__':
    dicionario = criar_dicionario()
    imprimir_dicionario(dicionario)
    
    imprimir_nome(dicionario)
    imprimir_idade(dicionario)
    imprimir_profissao(dicionario)