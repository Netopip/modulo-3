def funcao_mostrar_cubo(numero):
    return numero**3

def main():
    while True:
        try:
            numero = int(input('Digite um número inteiro:\n ').strip())
            print(f'O cubo de numero {numero} é {funcao_mostrar_cubo(numero)}')
            
            while True:
                opcao = input('Quer continuar? [S/N]:\n').upper().strip()
                if opcao in 'S':
                    break
                elif opcao in 'N':
                    print('Programa encerrado!')
                    return
                else:
                    print('Opção inválida!')
        
        except:
            print('Caractere inválido. Digite novamente!')
            
if __name__ == '__main__':
    main()