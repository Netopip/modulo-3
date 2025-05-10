def OrdemInversa(lista:list):
    listaInversa = []
    for _ in lista:
        if type(_) != int:
            return Exception
        else:
            listaInversa.insert(0,_)
    
    return listaInversa

assert OrdemInversa([1,2,3,4,5]) == [5,4,3,2,1] 

print('testes ok')
