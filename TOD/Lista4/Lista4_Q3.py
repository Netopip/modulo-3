def maior_elemento(numeros):
    maior = numeros[0]
    pos_maior = 0
    
    for posicao,numero in enumerate(numeros):
        if numero > maior:
            maior = numero
            pos_maior = posicao
            
    
    if numeros[pos_maior] + numeros[pos_maior - 1] > numeros[pos_maior] + numeros[pos_maior + 1]:
        return f'A maior soma é do {numeros[pos_maior]} na posição {pos_maior} com {numeros[pos_maior - 1]} na posição {pos_maior - 1} = {numeros[pos_maior] + numeros[pos_maior - 1]}'
    else:
        return f'A maior soma é do {numeros[pos_maior]} na posição {pos_maior} com {numeros[pos_maior + 1]} na posição {pos_maior + 1} = {numeros[pos_maior] + numeros[pos_maior + 1]}'
    


def main():
    numeros = [ ]
    
    while True:
        try:
            numero = int(input('Digige um numero:\n').strip())
            if numero == 0:
                break
            numeros.append(numero)
            
        except ValueError:
            print('Valor inválido')
    
    print(numeros)
    print(maior_elemento(numeros))
    
  
    

if __name__ == '__main__':
    main()