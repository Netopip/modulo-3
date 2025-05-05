import csv


dados_provedores = []

with open('TOPICOS/exerc fixação/internet/provedores.csv') as provedores:
    arquivo = csv.reader(provedores,delimiter=',')
    next(arquivo)
    for linha in arquivo:
        dados_provedores.append(linha)
        
def filtrarPorProvedor(dados):
    provedores = {}
    
    for linha in dados:
        if linha[0] not in provedores:
            provedores[linha[0]] = [provedor[1] for provedor in dados if provedor[0] == linha[0]]
            
    return provedores





#questao1:
questao1 = filtrarPorProvedor(dados_provedores)
for provedor,cidade in questao1.items():
    print(f'{provedor}: {cidade}')