def maximo(numero1,numero2,numero3,numero4):
    maior = numero1
    for i in (numero2,numero3,numero4):
        if i > maior:
            maior = i
    return maior
        

def verificar_numero():
    while True:
        try:
            numero = int(input('Digite o numero:\n').strip())
            return numero
            
        except ValueError:
            print(f'Digite um número inteiro válido')


            
def main():
    lista = []
    for i in range(4):
        numero_a = verificar_numero()
        numero_b = verificar_numero()
        numero_c = verificar_numero()
        numero_d = verificar_numero()

        maior = maximo(numero_a,numero_b,numero_c,numero_d)
        lista.append(maior)
        
        print(f'O maior número é: {maior}')
    print(f'O maior numero lido foi : {maximo(lista[0],lista[1],lista[2],lista[3])}')
    
         
if __name__ == '__main__':
    main()