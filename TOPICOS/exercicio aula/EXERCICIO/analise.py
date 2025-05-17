import numpy as np  


dados = np.genfromtxt('TOPICOS/exercicio aula/EXERCICIO/mudancas_climaticas.csv',delimiter=',',skip_header=1,dtype=None,encoding='utf-8')

def MediaTemperatura(dados):
    
    return round(np.mean([float(i[2]) for i in dados]),2)

def MediaCO2(dados):
        
    return round(np.mean([float(i[3]) for i in dados]),2)
    

def MediaPrecipitacao(dados):

    return round(np.mean([float(i[4]) for i in dados]),2)

def CidadeMaiorMediaTemperatura(dados):
    indiceMaior = 0
    maiorTemp = float(dados[0][2])
    for i in range(1, len(dados)):
        temp = float(dados[i][2])
        if temp > maiorTemp:
            maiorTemp = temp
            indiceMaior = i
    cidadeMaior = dados[indiceMaior][1] 
    return indiceMaior, cidadeMaior,maiorTemp
        
def CidadeMaiorCo2(dados):
    indiceMaior = 0
    maiorco2 = float(dados[0][3])
    for i in range(1,len(dados)):
        co2 = float(dados[i][3])
        if co2 > maiorco2:
            indiceMaior = i
            
    return dados[indiceMaior]

def ConverterTemperaturas(dados):
    temperaturaF = []
    for i in dados:
        temperatura = (float(i[2])*9/5)+32
        temperaturaF.append(round(temperatura,2))
    return temperaturaF
        
        
print(dados[:5])     
print(MediaTemperatura(dados))
print(MediaCO2(dados))
print(MediaPrecipitacao(dados))
print(CidadeMaiorMediaTemperatura(dados))
print(CidadeMaiorCo2(dados))
print(ConverterTemperaturas(dados))


    
    
    