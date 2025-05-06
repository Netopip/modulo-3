

def RetornarValorS(numero):
    if type(numero) != int or numero<=0:
        return Exception
    else:
        s = 0
        for _ in range(1,numero+1):
            s += 1/_
        
        return s
    
assert RetornarValorS(1) == 1
assert RetornarValorS(-1) == Exception
assert RetornarValorS(0) == Exception
assert RetornarValorS('a') == Exception
assert RetornarValorS(2) == 1.5
assert RetornarValorS(3) == 1.5 + 1/3
print('TESTES OK')