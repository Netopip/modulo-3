import csv
from modulo import calcularMedia



dados_carros = []
with open('TOPICOS/exerc fixação/carros/carros.csv',encoding='utf-8') as arquivo:
    carros = csv.reader(arquivo)
    next(carros)
    for linha in carros:
        dados_carros.append(linha)

    
      
def precoMedioPorMarca(dados):
    preco_medio = {}
    
    for linha in dados:
        if linha[0] not in preco_medio:
            preco_medio[linha[0]] = calcularMedia([float(veiculo[3]) for veiculo in dados if veiculo[0] == linha[0]]) 
    return preco_medio

def filtragemPorAno(dados):
    carros_ano = {}
    
    for linha in dados:
        if int(linha[2]) not in carros_ano:
            carros_ano[int(linha[2])] = [(carro[0],carro[1]) for carro in dados if(int(carro[2])) == int(linha[2])]
        
    return carros_ano

def filtraPorMotor(dados):
    carros_motor = {}
    
    for linha in dados:
        if linha[5] not in carros_motor:
            carros_motor[linha[5]] = [(carro[0],carro[1]) for carro in dados if carro[5] == linha[5]]

    return carros_motor

def filtroPorAnoPassado(dados,anos):
    carros_ano = {}
    
    for linha in dados:
        if linha[0] not in carros_ano:
            carros_ano[linha[0]] = [(carro[1],carro[2]) for carro in dados if(int(carro[2])) >= anos and carro[0] == linha[0]] 
            
    return carros_ano

def filtraPorMarca(dados):
    carros_marca = {}
    
    for linha in dados:
        if linha[0] not in carros_marca:
            carros_marca[linha[0]] = [(carro[0],carro[1],carro[2]) for carro in dados if carro[0] == linha[0]]
            
    return carros_marca
    

#imprimir os dados:
for j,linha in enumerate(dados_carros):
    print(f'{j+1}: {linha}')
print()
    

#- Calcule o preço médio dos veículos de cada marca.
questao2 = precoMedioPorMarca(dados_carros)
print(f'Preço medio por marca:')
for chave,valor in questao2.items():
    print(f'{chave}: média: {valor}')
print()
    
#Filtragem por ano de fabricação:
print('Filtragem por ano de fabricação:')
questao3 = filtragemPorAno(dados_carros)
for chave,valor in questao3.items():
    print(f'{chave}: {valor}\n')
print()
    
# Filtragem por tipo de motor:
print('Filtragem por tipo de motor:')
questao4 = filtraPorMotor(dados_carros)
for chave, valor in questao4.items():
    print(f'{chave}: {valor}\n')
print()

# fiotra pora ano passado:
questao5 = filtroPorAnoPassado(dados_carros,2020)
print('Filtragem por ano passado:')
for chave,valor in questao5.items():
    print(f'{chave}: {valor}')

print()

#filtro por marca:
questao6 = filtraPorMarca(dados_carros)
print('Filtragem por marca:')
for chave,valor in questao6.items():
    print(f'{chave}: {valor}')
    




