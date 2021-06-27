def criar_lista():
    lista = [1, 2, 3, 4, 5, 6]
    
    return lista
def criar_lista_nomes():
    lista = ["alice", "augusto", "alexandre", "lucas", "bruno"]
    
    return lista

def incrementar_lista_nomes(lista):
    lista.append("joão")

def remover_lista_nomes(lista, nome):
    lista.remove(nome)

def imprimir_lista(lista):
    for item in lista:
        print(item)

if __name__ == '__main__':
    # lista = criar_lista()
    # imprimir_lista(lista)
    
    lista1 = criar_lista_nomes()
    imprimir_lista(lista1)
    
    print("incrementando na lista de nomes...")
    
    incrementar_lista_nomes(lista1)
    imprimir_lista(lista1)
    
    print("removendo da lista Bruno...")
    
    remover_lista_nomes(lista1, "bruno")
    imprimir_lista(lista1)