def valor_s(n):
    s = 0
    for i in range(1,n+1):
        termo = (i**2 + 1) / (i + 3)
        s += termo
    return round(s, 2)
        


def main():
    while True:
        try:
            n = int(input('Digite um valor positivo e inteiro:\n').strip())
            if n <= 0:
                print('Número tem que ser positivo e inteiro.')
                continue
            
            s = valor_s(n)
            print(f'O valor de S é: {s}')
            break
            
            
        except ValueError:
            print('Digite um valor válido.')
            
if __name__ == '__main__':
    main()