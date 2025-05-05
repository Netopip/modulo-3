from random import *
import string


max_lista = 20

def gerar_lista():
    lista_alfabeto = [choice(string.ascii_letters.upper()) for _ in range(max_lista)]
    return lista_alfabeto

def verificar_letra(letra,lista):
    vezes = 0
    for i in lista:
        if letra == i:
            vezes += 1
    return vezes

def main():
    
    lista = gerar_lista()
    while True:
        letra = str(input('Digite uma letra:\n').strip()).upper()

        if letra in string.ascii_letters.upper():
            break
        else:
            print('Digite uma letra válida!')
            
            
    print(lista)
    vezes = verificar_letra(letra, lista)
    print(f'A letra {letra} aparece {vezes} vezes na lista')
    
if __name__ == "__main__":
    main()