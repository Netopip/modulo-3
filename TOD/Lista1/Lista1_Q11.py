def numero_divisores(numero):
    quantiade = 0
    for i in range(1,numero+1):
        if numero % i ==0 :
            quantiade += 1
    return quantiade
 

def main():
    while True:
        try:
            numero = int(input('Digite um numero interio:\n').strip())
            if numero < 0:
                print('O numero deve ser positivo.')
                continue
            
            print(f'A quantidade de divisores que o número {numero} possui é : {numero_divisores(numero)}.')
            break

        except:
            print('Digite um numero válido')
            
if __name__ == '__main__':
    main()