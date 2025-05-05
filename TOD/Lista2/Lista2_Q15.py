from random import *

max_lista = 10

def lista_inersa(lista):
    lista_inversa = []
    for i in range(len(lista)):
        lista_inversa.insert(0,lista[i])
    return lista_inversa

        
def main():
    lista_d = [randint(-100,100) for _ in range(10)]
    lsita_e = lista_inersa(lista_d)
    
    print("Lista original: ", lista_d)
    print("Lista inversa: ", lsita_e)

if __name__ == "__main__":
    main()
    