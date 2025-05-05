from random import *

max_lista = 10


def gerar_lista():
    lista = [round(uniform(-100,100),2) for _ in range(max_lista)]
    return lista

def verificar_lista(lista):
    quant_negativos = 0
    soma_positivos =0
    for i in lista:
        if i < 0:
            quant_negativos += 1
        else:
            soma_positivos += i
    return quant_negativos, soma_positivos

def main():
    lista = gerar_lista()
    print("Lista gerada:", lista)
    quant_negativos, soma_positivos = verificar_lista(lista)
    print("Quantidade de negativos:", quant_negativos)
    print("Soma dos positivos:", soma_positivos)
    
if __name__ == "__main__":  
    main()