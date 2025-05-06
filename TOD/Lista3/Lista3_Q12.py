

def SomatorioNumero(numero):
    if type(numero) != int or numero <= 0:
        return Exception
    else:
        soma = 0
        for _ in range(numero+1):
            soma += _
        
        return soma
    
assert SomatorioNumero(5) == 15
assert SomatorioNumero(1.45) == Exception
assert SomatorioNumero('') == Exception
assert SomatorioNumero(-1) == Exception
assert SomatorioNumero(0) == Exception
assert SomatorioNumero('´') == Exception
print('TESTSE - OK')