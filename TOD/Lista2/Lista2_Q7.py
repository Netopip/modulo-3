from random import *

max_lista = 20

def gerar_lista():
    lista = [round(randint(-100,100),2) for _ in range(max_lista)]
    return lista

def verificar_numero_lista(lista,numero):
    for i in lista:
        if i == numero:
            return True
        else:
            return False

def main():
    lista = gerar_lista()
    
    while True:
        try:
            numero = int(input('Digite um numero:\n').strip())
            if verificar_numero_lista(lista,numero):
                print(f'O número {numero} está na lista!')
                break
            else:
                print(f'O número {numero} não está na lista!')
                break
                
            
        except ValueError:
            print('Valor inválido!')
    
    print(lista)
            
if __name__ == "__main__":
    main()  