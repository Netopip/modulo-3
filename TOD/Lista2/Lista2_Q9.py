from random import *

max_lista = 5

def gerar_lista():
    lista = [round(uniform(0,100),2) for _ in range(max_lista)]
    return lista

def lista_y(lista):
    lista_y = []
    for i in lista:
        lista_y.insert(0,i)
    return lista_y

def main():
    lista = gerar_lista()
    print(f'Lista original: {lista}')
    lista_invertida = lista_y(lista)
    print(f'Lista invertida: {lista_invertida}')
    
if __name__ == '__main__':
    main()
        