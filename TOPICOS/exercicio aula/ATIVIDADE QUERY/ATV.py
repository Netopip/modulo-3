#feito por :
#Francisco Fernandes de Oliveira Neto
#Leomar Pereira de Lima 

import pandas as pd

def calcular_km_media(df, ano_atual):
    km_media = df['Quilometragem'] / (ano_atual - df['Ano'])
    return km_media

def verificar_nulos(dataset):
    print("\nVerificação de nulos. Tem alguma coluna com dados nulos?")
    col_nulos = dataset.isnull().sum() 
    print("Sim, colunas x quantidade:\n",col_nulos[col_nulos>0]) if col_nulos.sum()>0 else print("Não.")

def main():
    dataset = pd.read_csv("TOPICOS/exercicio aula/ATIVIDADE QUERY/carros.csv", sep=';')

    print("4. mostre o dataset\n")
    print(dataset)
    print("-*" * 30)

    print("5. mostre os tipos de dados do dataset: comando: dtypes. Quais os tipos de dados das colunas deste dataset?\n")
    print(dataset.dtypes)
    print("-*" * 30)

    print("6. mostre a estatística descritiva das colunas: quilometragem e valor. Qual o significado dessas informações?\n")
    print(dataset[['Quilometragem', 'Valor']].describe())        
    print("-*" * 30)


    print("7. Obtenha mais informações do dataset com a função info(). Tem alguma coluna com dados nulos? Se sim, qual a coluna e quantos  dados nulos possui?\n")
    print(dataset.info())
    verificar_nulos(dataset)
    print("\nSubstuição NaN por Zero (0). Nova verificação:")
    dataset.fillna(0, inplace=True)
    verificar_nulos(dataset)
    print("-*" * 30)

    print('''
    8. Com base no Dataset que estamos trabalhando, defina uma função para mostrar a quilometragem média de todos os carros.  Sabendo  que a formula é:
    
        Km_media = km_total / (ano_atual - ano_fabricação)

    A função tem que receber como parâmetros: o dataset e o ano atual.
    Execute a função e mostre o resultado.\n''')
    ano_atual = 2025
    dataset['KM_media'] = calcular_km_media(dataset, ano_atual)
    print(dataset[['Nome', 'Quilometragem', 'Ano', 'KM_media']])
    print("-*" * 30)

    print("9. Utilizando a pesquisa com queries, faça:")
    print('\na) mostre os carros com motor "Diesel V8\n')
    print(dataset.query('Motor == "Motor Diesel V8"'))
    print('\nb) pesquise por carros com motor 1.0 8v usados com preço inferior a R$ 100.000\n')
    print(dataset.query('Motor == "Motor 1.0 8v" and Zero_km == False and Valor < 100000'))
    print('\nc) pesquise por carros com km média de até 10.000 km com Motor 1.8 16v\n')
    print(dataset.query('KM_media <= 10000 and Motor == "Motor 1.8 16v"'))
    print('\nd) liste os tipos de motores cadastrados\n')
    print(dataset['Motor'].unique())
    print('\ne) liste os carros com câmbio automático com valor abaixo de R$ 100.000\n')
    print(dataset.query('Acessórios.str.contains("Câmbio automático") and Valor < 100000'))
    print('\nf) liste os carros novos com "freios ABS" que custam acima de R$ 100.000\n')
    print(dataset.query('Zero_km == True and Acessórios.str.contains("Freios ABS") and Valor > 100000'))
    print('\ng) liste os carros novos ou usados com km média abaixo de 10.000 km que custam até R$ 100.000\n')
    print(dataset.query('KM_media < 10000 and Valor < 100000'))
    


if __name__ == '__main__':
    main()
