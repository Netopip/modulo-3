import csv
from modulo_tabela import calcular_media

dados_gerais = []
with open('TOPICOS/exerc fixação/tabela/tabela.csv') as arquivo_csv:
    arquivo = csv.reader(arquivo_csv)
    next(arquivo)
    for linha in arquivo:
        dados_gerais.append(linha)

print(dados_gerais)


def cidades_por_estado(dados):
    cidades_estados = {}
    print('Aqui estaõ as cidades agrupadas por Estados:')
    
    for linha in dados:
        if linha[1] not in cidades_estados:
            cidades_estados[linha[1]] = [cidade[0] for cidade in dados if cidade[1] == linha[1]]
    
    return cidades_estados

def populocao_por_estado(dados):
    populacao_estado = {}
    
    for linha in dados:
        if linha[1] not in populacao_estado:
            populacao_estado[linha[1]] = sum([int(cidade[2]) for cidade in dados if cidade[1] == linha[1]])
    
    return populacao_estado

def estado_maior_populacao(dados):
    print('O estado com maior população:')
    maior_pop = 0
    estado_maior = ''
    
    populacao = populocao_por_estado(dados)
    for estado,populacao in populacao.items():
        if populacao > maior_pop:
            maior_pop = populacao
            estado_maior = estado
            
    return estado_maior, maior_pop

def media_popu_estado(dados):
    media_por_estado = {}
    
    for linha in dados:
        if linha[1] not in media_por_estado:
            media_por_estado[linha[1]] = calcular_media([int(cidade[2]) for cidade in dados if cidade[1] == linha[1]])
        
       
    return media_por_estado


#estado com maior área:
def estado_maior_area(dados):
    maior_area = 0
    estado_maior = ''
    
    for linha in dados:
        if float(linha[3]) > maior_area:
            maior_area = float(linha[3])
            estado_maior  = linha[1]
            
    return estado_maior,maior_area

#cidades grandes por estado:
def cidades_grande_estado(dados):
    cidades_grandes = {}
    
    for linha in dados:
        if linha[1] not in cidades_grandes:
            cidades_grandes[linha[1]] = [[cidade[0],cidade[2]] for cidade in dados if int(cidade[2]) > 1000000 and cidade[1] == linha[1]] 
            
    return cidades_grandes

#questão cidade por estado:
questao1 = cidades_por_estado(dados_gerais)
for chave, valor in questao1.items():
    print(f'{chave}: {valor}')
print()
    
#questao populacao por estado:
questao2 = populocao_por_estado(dados_gerais)
print('Aqui estão as populações por estado:')
for estado,populacao in questao2.items():
    print(f'{estado}: {populacao}')
print()
    
#questao estado maior populaçao:
questao3 = estado_maior_populacao(dados_gerais)
print(questao3)
print()
#questao meida por estado:
questao4 = media_popu_estado(dados_gerais)
print('Aqui estão as médias por estado:')
for chave,valor in questao4.items():
    print(f'{chave}: {valor}')
    
#questao estado maior area:
questao5 = estado_maior_area(dados_gerais)
print('Aqui estão os estados com maior área:')
print(f'{questao5[0]}: {questao5[1]}')
print()

#questao cidades grande por estado:
questao6 = cidades_grande_estado(dados_gerais)
print('Cidades grande por Estado:')
for chave,valor in questao6.items():
    print(f'{chave}: {valor}')
