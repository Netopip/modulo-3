
def calcular_peso_ideal(codigo,altura):
    if codigo == '1':
        peso_ideal = (62.1*altura)-44.7
    elif codigo == '2':
        peso_ideal = (72.7*altura)-58
    return round(peso_ideal,2)


def main():
    while True:
        try:
            altura = float(input('Digite a altura: \n').strip())
            sexo = str(input('Digite o sexo [1-Feminino|2-Masculino]: \n').strip())
            
            if sexo != '1' and sexo != '2':
                print('Digite somente 1 ou 2.')
                continue
            
            print(f'Seu peso idela é {calcular_peso_ideal(sexo,altura)}.')
            break
        
        except:
            print('Digite um numero válido.')
            
            
if __name__ == '__main__':
    main()