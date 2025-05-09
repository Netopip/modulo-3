
def verificarPoligono(NumerodeLados,medidaLado):
    try:
        NumerodeLados = int(NumerodeLados)
        medidaLado = int(medidaLado)
        if medidaLado <= 0:
            return Exception
        else:
            if NumerodeLados == 3:
                perimetro = NumerodeLados * medidaLado
                return f'TRIANGULO : {perimetro}'
            elif NumerodeLados == 4:
                perimetro = NumerodeLados * medidaLado
                return f'QUADRADO : {perimetro}'
            elif NumerodeLados == 5:
                perimetro = NumerodeLados * medidaLado
                return f'PENTAGONO : {perimetro}'
            else:
                return Exception
    
    except ValueError:
        return Exception

assert verificarPoligono(4,4) == 'QUADRADO : 16'
assert verificarPoligono(3,2) == 'TRIANGULO : 6'
assert verificarPoligono(5,5) == 'PENTAGONO : 25'
assert verificarPoligono(5,'a') == Exception
assert verificarPoligono(0,1) == Exception
assert verificarPoligono(3,0) == Exception
assert verificarPoligono(6,3) == Exception
assert verificarPoligono(0,0) == Exception
assert verificarPoligono('a','b') == Exception
assert verificarPoligono('','') == Exception

print('testes - ok')