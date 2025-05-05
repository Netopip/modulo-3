from random import *

max_lista =20

def gerar_lista_preco():
    lista_preco = [round(uniform(1,100),2) for _ in range(max_lista)]
    return lista_preco

def gerar_lista_quant():
    lista_quant = [randint(1,100) for _ in range(max_lista)]
    return lista_quant

def calcular_faturamento(lista_preco,lista_quant):
    faturamento = []
    for i in range(len(lista_preco)):
        faturamento.append(lista_preco[i] * lista_quant[i])
    
    return faturamento

def total_faturamento_media(faturamento):
    total = 0
    for i in faturamento:
        total += i
    media = total / len(faturamento)
    
    return total,media

def faturamento_abaixo_media(faturamento,media):
    abaixo_media = []
    for i in faturamento:
        if i< media:
            abaixo_media.append(i)
    return abaixo_media

    
def main():
    lista_1 = gerar_lista_preco()
    lista_2 = gerar_lista_quant()
    
    
    faturamento = calcular_faturamento(lista_1,lista_2)
    total_faturamento,media = total_faturamento_media(faturamento)
    abaixo_media = faturamento_abaixo_media(faturamento,media)
    
    print(f"Faturamento total: {total_faturamento:.2f}")
    print(f"Média de faturamento: {media:.2f}")
    print(f'Faturamento abaixo da média: {abaixo_media}')
    
    
if __name__ == "__main__":
    main()
    
        
       