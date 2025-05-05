from random import *

max_lista = 3

def gerar_lista():
    lista = [round(uniform(-100,100),2) for _ in range(max_lista)]
    return lista

def intercalar_listas(lista1,lista2):
    lista_intercalada = list(range(max_lista *2))
    
        #primeira versão
    '''for i in range(len(lista1)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])'''
        
    #segunda versão   
    cont = 0 
    for i in range(len(lista_intercalada)):
        if i%2 == 0:
            lista_intercalada[i] = lista1[cont]
        else:
            lista_intercalada[i] = lista2[cont]
            cont += 1
    
    return lista_intercalada

def main():
    lista1 = gerar_lista()
    lista2 = gerar_lista()
    
    lista_inter = intercalar_listas(lista1, lista2)
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Lista Intercalada: {lista_inter}")
    
if __name__ == "__main__":
    main()
        
        
