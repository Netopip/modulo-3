def verificar_lista(lista):
    pass
   
        
    


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
                
    
    
if __name__ == "__main__":
    main()