def calcular_s(valor):
    total = 0
    for i in range(1, valor+1):
        total += 1/i
    return total



def main():
    while True:
        try:
            valor = int(input('Digite um valor inteiro e positivo:\n').strip())
            if valor <= 0 :
                continue
            
            total = calcular_s(valor)
            print(f'O valor de S é {total:.2f}.')
            break
                
        except ValueError:
            print('Valor inválido. Tente novamente.')
            
if __name__ == '__main__':
    main()