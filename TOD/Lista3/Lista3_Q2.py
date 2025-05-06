import math 

def calcular_raio(raio):
    try:
        raio = float(raio)
        if raio <= 0:
            return Exception
        else:
            return round(round(math.pi,2) * (raio **2),2)
    
    except ValueError:
        return Exception
    
def calcular_perimetro(raio):
    try:
        raio = float(raio)
        if raio <= 0:
            return Exception
        else:
            return round(round(math.pi,2) * (raio * 2),2)
    
    except ValueError:
        return Exception
    
assert calcular_raio(2) == 12.56
assert calcular_raio(0) == Exception
assert calcular_raio(-2) == Exception
assert calcular_raio('a') == Exception
assert calcular_perimetro(2) == 12.56
assert calcular_perimetro(0) == Exception
assert calcular_perimetro('a') == Exception
assert calcular_perimetro(-2) == Exception
assert calcular_perimetro(3) == 18.84
print('TESTES - ok')