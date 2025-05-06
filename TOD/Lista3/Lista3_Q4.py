

def calcular_media(notaA,notaB):
    try:
        notaA = float(notaA)
        notaB = float(notaB)
        if (notaA < 0 or notaA > 10) or ( notaB < 0 or notaB > 10):
            return Exception

        media = round((notaA + notaB) /2,2)
        if media >=6:
            return "PARABÉNS! Você foi aprovado!"
        else:
            return
    
    except ValueError:
        return Exception

assert calcular_media(10,8) == "PARABÉNS! Você foi aprovado!"
assert calcular_media(5,4) == None
assert calcular_media(10,10) == "PARABÉNS! Você foi aprovado!"
assert calcular_media(10,0) == None
assert calcular_media('a',0) == Exception
assert calcular_media(5,11) == Exception
assert calcular_media(0,0) == None
print('TESTES - ok')
