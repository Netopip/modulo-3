def calcular_numeros(numero1,numero2):
    soma = 0
    for i in range(numero1,numero2+1):
        soma += i
    return soma
        
        
def main():
    while True:
        try:
            numero_1 = int(input('Digite o primeiro numero:\n').strip())
            numero_2 = int(input('Digite o segundo numero:\n').strip())
            
            if numero_1 > numero_2:
                print('O segundo numero tem que ser maior que o primeiro!')
                continue
            
            print(f'A soma dos numeros no intervalo de {numero_1} e {numero_2} é {calcular_numeros(numero_1,numero_2)}')
            break
            
        except ValueError:
            print('Digite um numero inteiro válido!')
            
if __name__ == '__main__':
    main()
            
        
            
            
            