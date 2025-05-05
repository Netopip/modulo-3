from random import *

max_lista = 15

def gerar_lista():
    lista = [round(uniform(-100,100),2) for i in range(max_lista)]
    return lista


def maior_menor(lista):
    maior = lista[0]
    menor = lista[1]
    posicao_maior= 0
    posicao_menor = 1
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            posicao_maior = i
        elif lista[i] < menor:
            menor = lista[i]
            posicao_menor = i
    
    return maior,menor,posicao_maior,posicao_menor


    

def main():
    lista = gerar_lista()
    print(f'Lista: {lista}')
    maior,menor,posicao_maior,posicao_menor = maior_menor(lista)
    print(f'O maior elemento {maior} na posição {posicao_maior}\ne o menor é {menor} na posição {posicao_menor}.')
    
if __name__ == "__main__": 
    main()



