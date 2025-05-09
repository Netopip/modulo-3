def fatorial(numero):
    result = 1
    for i in range(1,numero+1):
        result *= i
    return result
    
    
def RetornarValorS(numero):
    if type(numero) != int or numero<=0:
        return Exception
    else:
        s = 1
        for _ in range(1,numero+1):
            s += 1/fatorial(_)
        
        return s
    
assert RetornarValorS(1) == 2
assert RetornarValorS(2) == 2.5
assert RetornarValorS(0) == Exception
assert RetornarValorS('a') == Exception
assert RetornarValorS(' ') == Exception
print('TESTE OK')