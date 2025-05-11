def ListaNumeros(lista:list):
    maior = lista[0]
    posicaoMaior = lista[0]
    menor = lista[0]
    posicaoMenor = lista[0]
    for _ in range(len(lista)):
        if type(lista[_]) != int or len(lista)<15 or len(lista)>15:
            return Exception
        else:
            if lista[_] > maior:
                maior = lista[_]
                posicaoMaior = _
            elif lista[_] < menor:
                menor = lista[_]
                posicaoMenor = _
                
    return maior,posicaoMaior,menor,posicaoMenor
    
                
        

assert ListaNumeros([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]) == (14,14,0,0)
assert ListaNumeros([-10,20,15,30,45,4857,-15,-2035,6,98,702,11,23,65,4]) == (4857,5,-2035,7)
assert ListaNumeros(['',4,2,3,5,-15,54,12,15,3,25,6,3,2,1]) == Exception
assert ListaNumeros([7,4,2,3,5,-15,54.5,12,15,3,25,6,3,2,1]) == Exception

print('testes ok')

            
            