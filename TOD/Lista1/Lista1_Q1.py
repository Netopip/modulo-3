def verificar_numero(n):
    if n%2 == 0:
        return True
    else:
        return False


def main():
    while True:
        try: 
            numero = int(input("Insira um número:\n").strip())
            if verificar_numero(numero):
                print(f'\nO número {numero} é PAR.')
            else:
                print(f'\nO número {numero} é ÍMPAR.')
            break
        
        except:
            print(f'Valor inválido. Insira um número inteiro.')
            
if __name__ == '__main__':
    main()