

def pesoIdeal(altura,sexo):
    try:
        altura = float(altura)
        sexo = int(sexo)
        if sexo == 1:
            return round(((62.1 * altura) - 44.7),2)
        elif sexo == 2:
            return round(((72.7 * altura)-58),2)
        else:
            return Exception
    
    except ValueError:
        return Exception

assert pesoIdeal(1.75,1) == 63.97
assert pesoIdeal(1.75,3) == Exception
assert pesoIdeal(1.75,'a') == Exception
assert pesoIdeal(1.75,'1') == 63.97
assert pesoIdeal(1.63,2) == 60.50 
assert pesoIdeal(1.63,1) == 56.52

print('testes ok')