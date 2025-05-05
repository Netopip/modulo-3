from random import *

max_lista = 15

def gerar_lista():
    lista = [randint(1,100) for _ in range(max_lista)]
    return lista

def maior_menor_lista(lista):
    maior = lista[0]
    menor = lista[0]
    posicao_maior = 0   
    posicao_menor = 0
    for _ in range(len(lista)):
        if lista[_]> maior:
            maior = lista[_]
            posicao_maior = _
    for _ in range(len(lista)):
        if lista[_]< menor:
            menor = lista[_]
            posicao_menor = _
    
    return maior,menor,posicao_maior,posicao_menor

if __name__ == '__main__':
    lista = gerar_lista()
    maior,menor,posicao_maior,posicao_menor = maior_menor_lista(lista)
    print(f'A lista gerada: {lista}')
    print(f'O maior elemento da lista é {maior} e está na posição {posicao_maior}')
    print(f'O menor elemento da lista é {menor} e está na posição {posicao_menor}')
    