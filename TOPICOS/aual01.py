import csv


def pessoas_cidades(lista,cidade):
    pessoas =[]
    print(f'Pessoas que mmoram em {cidade}:')
    for i in lista:
        if i[2] == cidade:
            pessoas.append(i[0])
    
    return pessoas

def pessoas_idade_maior(lista,x):
    print(f'Pessoas com idade maior que {x} anos agrupada por cidade:')
    dic_pessoas = {}
    
    for i in lista:
        if i[2] not in dic_pessoas:
            dic_pessoas[i[2]] = [pessoas for pessoas in lista if int(pessoas[1]) > x and pessoas[2] == i[2]]

    return dic_pessoas


def pessoa_faixa(lista,x,y):
    print(f'Pessoas com idade entre {x} e {y} anos agrupadas por cidades:')
    pessoas_faixa_idade= {}
    
    for i in lista:
        if i[2] not in pessoas_faixa_idade:  
            pessoas_faixa_idade[i[2]] = [pessoa for pessoa in lista if int(pessoa[1]) >= x and int(pessoa[1]) <= y and pessoa[2] == i[2]]  
    
    return pessoas_faixa_idade
             
def media(lista):
    media = sum(lista)/len(lista)
    return round(media,2)
    
         
def media_idade_pessoa(lista):
    print(f'Média de idade  por cidades:')
    dic_media_cidade = {}
    
    for i in lista:
        if i[2] not in dic_media_cidade:
            dic_media_cidade[i[2]] = media([int(pessoa[1]) for pessoa in lista if pessoa[2] == i[2] ])
        
    return dic_media_cidade
        


lista_com_dados = []
with open('TOPICOS/pessoas.csv') as file:
    arq = csv.reader(file) 
    next(arq)
    for linha in arq:
        lista_com_dados.append(linha)
        
    

#letra A
print(pessoas_cidades(lista_com_dados,'Fortaleza'))
print()
print()

#letra B
pessoas_maiores = (pessoas_idade_maior(lista_com_dados,30))
for chave, valor in pessoas_maiores.items():
    print(f'{chave}: {valor}')
print()
print()

#letra C

pessoa_intervalo = (pessoa_faixa(lista_com_dados,20,30))
for chave,valor in pessoa_intervalo.items():
    print(f'{chave} : {valor}')
print()
print()


#letra D
media_idade = (media_idade_pessoa(lista_com_dados))
for chave,valor in media_idade.items():
    print(f'{chave}: tem media de {valor} anos.')
