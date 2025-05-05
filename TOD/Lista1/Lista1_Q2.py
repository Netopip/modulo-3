import math

def calcular_area(r):
    area = math.pi * (r ** 2)
    return round(area,2)

def calcular_perimetro(r):
    perimetro = 2 * math.pi * r
    return round(perimetro,2)

def main():
    while True:
        try:
            raio = float(input('Insira um número:\n').strip())
            print(f'A área do círculo de raio {raio} é: {calcular_area(raio)}.\n')
            print(f'O perímetro do círculo de raio {raio} é: {calcular_perimetro(raio)}.')
            break
            
        except:
            print(f'Valor inválido.Tente novamente.')

if __name__ == '__main__':
    main()     
        
        