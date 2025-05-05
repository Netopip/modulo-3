from random import *

max_lista = 10

def copiar_negativos(lista):
    lista_r = []
    for i in lista:
        if i < 0:
            lista_r.append(i)
    return lista_r
            
def main():
    lista_x = [randint(-100,100) for _ in range(max_lista)]
    lista_r = copiar_negativos(lista_x)
    
    print(lista_x)
    print(lista_r)
    
if __name__ == "__main__":
    main()
    
    