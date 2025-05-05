def calcular_valores(n_lados,medida_lado):
    if n_lados == 3:
        perimetro = medida_lado * 3
        return f'TRIANGULO\nPerimetro: {perimetro}cm'
    elif n_lados == 4 :
        area = medida_lado**2
        return f'QUADRADO\nArea: {area}cm'
    elif n_lados == 5:
        return 'PENTAGONO'


def main():
    while True:
        try:
            lados = int(input('Digite o numero de lados do poligono:\n').strip())
            medida_lado = float(input('Digite o valor do lado em cm:\n').strip())
            
            if lados < 3 or lados > 5:
                print('Digite o lado no intervalo de 3 a 5')
                continue
            
            print(calcular_valores(lados,medida_lado))
            break
        
        except:
            print('Digite um valor válido')
            
if __name__ == '__main__':
    main() 
        