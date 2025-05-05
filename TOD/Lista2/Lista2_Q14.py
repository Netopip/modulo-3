from random import *

def lista_c_mod(lista):
    lista_c = lista.copy()
    for _ in range(len(lista_c)):
        if lista_c[_] < 0:
            lista_c[_] = 0
            
    return lista_c

def main():
    lista_c = [randint(-100,100) for _ in range(10)]
    lista_c_modificada = lista_c_mod(lista_c)
    print(f'Lista original: {lista_c}')
    print(f'Lista modificada: {lista_c_modificada}')
    
if __name__ == '__main__':
    main()


