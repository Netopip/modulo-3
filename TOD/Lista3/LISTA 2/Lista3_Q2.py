def ListaNumerosReais(lista:list):
    cont_negativos = 0
    soma_positivos = 0
    for _ in lista:
        if type(_) != int or len(lista) < 10 or len(lista)>10:
            return Exception
        else:
            if _ < 0:
                cont_negativos += 1
            else:
                soma_positivos += _

    return cont_negativos,soma_positivos

assert ListaNumerosReais([1,2,3,4,5,6,7,8,9,10,11]) == Exception
assert ListaNumerosReais([1,2,3,4,5]) == Exception
assert ListaNumerosReais([-1,21,2.5,6,-10,8,9,7,3,8]) == Exception
assert ListaNumerosReais(['a','b','c','',4,9,8,7,8,2]) == Exception
assert ListaNumerosReais([-1,-2,-3,1,2,3,4,5,6,7]) == (3,28)

print('testes ok')