def Fahrenheit_para_Celsius(Temperatura):
    C = ((Temperatura-32)/9)*5
    return round(C,1)


def main():
    while True:
        try:
            temperatura = float(input('Digite a temperatura em F°:\n').strip())
            print(f'A temperatura {temperatura} F° em Celsius é {Fahrenheit_para_Celsius(temperatura)}C°.')
            break
        except:
            print('Valor inválido, tente novamente!')
            
if __name__ == '__main__':
    main()
    