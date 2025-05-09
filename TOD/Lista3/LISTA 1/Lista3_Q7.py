def calcularFatorial(numero):
    if (type(numero) != int) or numero <=0:
        return Exception
    
    else:
        cont = 1
        for i in range(1,numero+1):
            cont *= i
            
        return cont

assert calcularFatorial(5) == 120
assert calcularFatorial(1) == 1
assert calcularFatorial(6) == 720
assert calcularFatorial(0) == Exception
assert calcularFatorial('') == Exception
assert calcularFatorial('a') == Exception
assert calcularFatorial(1.45) == Exception


print('TESTES - ok')
    