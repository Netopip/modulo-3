def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def main():
    while True:
        try:
            numero = int(input('Digite um numero para obter o fatorial:\n').strip())
            if numero < 1:
                print('Digite um numero interio maior que 1.')
                continue
            else:
                print(f'O fatorial de {numero} é {calcular_fatorial(numero)}.')
                break
        
        except ValueError:
            print('Digite um numero interio válido.')
            
if __name__ == '__main__':
    main()
                