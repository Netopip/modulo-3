def eliminar_repetidos(numeros):
    numeros_nao_repitidos = [ ]
    for numero in numeros:
        if numero not in numeros_nao_repitidos:
            numeros_nao_repitidos.append(numero)
    
    return numeros_nao_repitidos
    


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
    numeros_sem_rp = eliminar_repetidos(numeros)
    print(numeros_sem_rp)
    
if __name__ == '__main__':
    main()    