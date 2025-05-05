from random import *


max_lista = 10

def gerar_lista():
    lista = [round(uniform(-100,100),2) for i in range(max_lista)]
    return lista

def inverso_lista(lista):
    lista_inversa = []
    for i in lista:
        lista_inversa.insert(0,i)
    
    return lista_inversa

def main():
    lista = gerar_lista()
    print("Lista original: ", lista)
    lista_inversa = inverso_lista(lista)
    print("Lista inversa: ", lista_inversa)
    
if __name__ == "__main__":
    main()  
    
        