def verificar_lista(lista):

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True
            
    


def main():
    lista = []
    
    while True:
        try:
            num = int(input('Digite um numero:\n').strip())
            if num == 0:
                break
            lista.append(num)
        except ValueError:
            print('Valor inválido. Tente novamente.')
                
    print(verificar_lista(lista))
    
    
if __name__ == "__main__":
    main()