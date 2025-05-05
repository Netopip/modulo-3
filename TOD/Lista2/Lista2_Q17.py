from random import *



max_lista = 10

def verificar_valor_na_lista(lista,valor):
    vezes = 0
    for i in lista:
        if i == valor:
            vezes += 1
    
    return vezes
        
    


def main():
    lista_w = [randint(1,10) for _ in range(max_lista)]
    while True:
        try:
            valor_v = int(input('Digite um numero no intervalo de 1 a 10\n').strip())
            if valor_v < 1 or valor_v >10:
                print('Valor deve estar entre 1 e 10')
                continue
            else:
                vezes = verificar_valor_na_lista(lista_w,valor_v)
                print(lista_w)
                print(f'O valor {valor_v} apareceu {vezes} na lista')
                break
        except ValueError:
            print(f'Valor inválido.Tente novamente')
            
    print(f'Fim do programa.')
    
if __name__ == '__main__':
    main()