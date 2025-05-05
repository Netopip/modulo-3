def somatorio(numero):
    cont  = 0
    for i in range(numero,0,-1):
        cont += i
    return cont



    
def main():
    while True:
        try:
            numero = int(input('Digite um numero interio positivo.\n').strip())
            if numero < 0:
                print('Numero não pode ser menor que zero!')
                continue
            
            print(somatorio(numero))
            break
        except ValueError:
            print(f'Digite um numero válido')
        
if __name__ == '__main__':
    main()
    