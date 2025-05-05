def fatorial(n):
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= i
    return fatorial


def calcular_s(n):
    s = 1
    for i in range(1, n+1):
        s += 1 / fatorial(i) 
    return round(s,4)

def main():
    while True:
        try:
            n = int(input('Digite um valor positivo e inteiro:\n').strip())
            if n <= 0:
                print('Número tem que ser positivo e inteiro.')
                continue
            
            print(f' O valor de S é {calcular_s(n)}.')
            break
        
        except ValueError:
            print('Digite um valor válido.')
            
if __name__ == '__main__':
    main()
    