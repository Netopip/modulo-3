def calcular_media(nota1,nota2):
    media = (nota1+nota2)/2
    return round(media,2)

def main():
    while True:
        try:
            nota1 = float(input('Digite a primeira nota: \n').strip())
            nota2 = float(input('Digite a segunda nota: \n').strip())
            
            if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
                print('As notas devem estar entre 0 e 10. Tente novamente.')
                continue
            
            media = calcular_media(nota1,nota2)
            if media>=6:
                print(f'PARABÉNS! Você foi aprovado com média {media}.')
            else:
                print(f'Você foi reprovado com média {media}.')
            break
        
        except:
            print('Digite um número válido.')

if __name__ == '__main__':
    main()            