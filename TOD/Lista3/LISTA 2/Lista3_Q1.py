from random import *

def listaElementos(listaNumeros:list):
    lista_par = []
    lista_impar = []
    cont_par = 0
    cont_impar = 0
    
    lista = listaNumeros
    for i in lista:
        if type(i) != int:
            return Exception
        else:
            if i%2 == 0:
                lista_par.append(i)
                cont_par +=1
            else:
                lista_impar.append(i)
                cont_impar += 1
    
    return lista_par,lista_impar,cont_par,cont_impar

assert listaElementos([1,2,3,4,5]) == ([2,4],[1,3,5],2,3)
assert listaElementos([0,1,2,3,4,5,6,7,8,9,10]) == ([0,2,4,6,8,10],[1,3,5,7,9],6,5)
assert listaElementos([1,2,'a',4,5,6]) == Exception
assert listaElementos(['',2,3,4,5,6]) == Exception
assert listaElementos([1,2,3.5,4,5,6]) == Exception

print('testes OK')
            
    


        
    
    

