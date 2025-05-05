def contagem_numeros(numeros):
    contagem = {}
    
    for numero in numeros:
        if numero in contagem:
            contagem[numero] += 1
        else:
            contagem[numero] = 1
    
    return contagem
    
    
    
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
    contagem = contagem_numeros(numeros)
    print(contagem)
   
    
    
if __name__ == '__main__':
    main()    