

def SomaIntervalo(numeroA , numeroB):
    if (type(numeroA) != int) or (type(numeroB) != int) or (numeroA > numeroB):
        return Exception
    else:
        soma = 0
        for i in range(numeroA,numeroB+1):
            soma += i
        return soma
    
    
assert SomaIntervalo(2,5) == 14
assert SomaIntervalo(5,2) == Exception
assert SomaIntervalo(-1,3) == 5
assert SomaIntervalo('','b') == Exception
assert SomaIntervalo(1.5,5) == Exception
print('TESTES - OK')