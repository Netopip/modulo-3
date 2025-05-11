
maxElementos = 5

def IntercalarLista(lista1:list,lista2:list):
    if len(lista1) != maxElementos or len(lista2) != maxElementos:
        return Exception
        
    listaIntercalada = []
    for i in range(len(lista1)):
        if type(lista1[i]) != int or type(lista2[i]) != int:
            return Exception
        else:
            listaIntercalada.append(lista1[i])
            listaIntercalada.append(lista2[i])
            
    return listaIntercalada

assert IntercalarLista([0,1,2,3,4],[5,6,7,8,9]) == [0,5,1,6,2,7,3,8,4,9]
print('testes ok')
    
