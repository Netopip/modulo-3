

def retornarValorS(numero):
    if type(numero) != int or numero < 1:
        return Exception
    else:
        s = 0
        for i in range(1,numero+1):
            termo = (i**2 + 1) / (i + 3)
            s += termo
        return round(s, 2)

assert retornarValorS(2) == 1.5
assert retornarValorS(1) == 0.5
assert retornarValorS('' ) == Exception
assert retornarValorS('a') == Exception
assert retornarValorS(1.5) == Exception
assert retornarValorS(0) == Exception
assert retornarValorS('*') == Exception
print('Teste ok')