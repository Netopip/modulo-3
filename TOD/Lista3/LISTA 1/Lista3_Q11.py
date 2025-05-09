
def NumeosDivisores(numero):
    if type(numero) != int or numero<=0:
        return Exception
    else:
        cont = 0
        for i in range(1, numero+1):
            if numero%i ==0:
                cont+=1

        return cont
    

assert NumeosDivisores(0) == Exception 
assert NumeosDivisores(-1) == Exception
assert NumeosDivisores(2.57) == Exception
assert NumeosDivisores(5) == 2
assert NumeosDivisores(40) == 8
print('TESTSE-OK')