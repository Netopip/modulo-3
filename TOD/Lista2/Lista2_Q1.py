from random import *


max_lista = 100

def gravar_lista():
    lista = [randint(-100,100) for _ in range(max_lista)]
    return lista

def listas_pares_impares(lista):
    lista_pares = []
    lista_impares = []
    quant_pares = 0
    qiant_impares =0
    for i in lista:
        if i%2==0:
            lista_pares.append(i)
            quant_pares += 1
        else:
            lista_impares.append(i)
            qiant_impares += 1
    return lista_pares,quant_pares,lista_impares,qiant_impares
            
def main():
    lista = gravar_lista()
    lista_pares,quant_pares,lista_impares,quant_impares = listas_pares_impares(lista)
    print(f'Listas: {lista}')
    print(f'Lista pares: {lista_pares}')
    print(f'Lista impares: {lista_impares}')
    print(f'Quantidade de pares: {quant_pares}')
    print(f'Quantidade de impares: {quant_impares}')
    
if __name__ == "__main__":
    main()
            