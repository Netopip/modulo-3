from random import *

def ocorrencias(lista):
    face1 = 0
    face2 = 0
    face3 = 0
    face4 = 0
    face5 = 0
    face6 = 0
    for i in range(len(lista)):
        if lista[i] == 1:
            face1 += 1
        elif lista[i] == 2:
            face2 += 1
        elif lista[i] == 3:
            face3 += 1
        elif lista[i] == 4:
            face4 += 1
        elif lista[i] == 5:
            face5 += 1
        elif lista[i] == 6:
            face6 += 1
    return face1, face2, face3, face4, face5, face6

def main():
    vezes = randint(1,100)

    lista_resultado = [randint(1,6) for i in range(vezes)] 
    print(f'Foi lançado {vezes} .')
    print(f'Os números sorteados foram: {lista_resultado}')
    
    face1, face2, face3, face4, face5, face6 = ocorrencias(lista_resultado)
    print(f'Face 1: {face1}')
    print(f'Face 2: {face2}')
    print(f'Face 3: {face3}')
    print(f'Face 4: {face4}')
    print(f'Face 5: {face5}')
    print(f'Face 6: {face6}')

if __name__ == '__main__':
    main()
    