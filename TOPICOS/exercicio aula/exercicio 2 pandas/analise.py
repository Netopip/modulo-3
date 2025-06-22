#feito por :
#Francisco Fernandes de Oliveira Neto
#Leomar Pereira de Lima 

import pandas as pd


def analisar_csv(csv):
    dados = pd.read_csv(csv,sep=';')
    
    print(dados.head())
    print(dados.tail())
    print(dados.shape)
    print(dados.info())
    print(dados.describe())
    print(dados.loc[:,['ORIGEM','DESTINO']].head())
    
analisar_csv('C:/Users/ferna/OneDrive/Desktop/IFPI3/TOPICOS/exercicio aula/exercicio 2 pandas/200601.CSV')