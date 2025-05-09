

def fahrenheitCelsius(temperatura):
    try:
        temperatura = float(temperatura)
        temp_celsius = ((temperatura - 32)/9)*5
        return temp_celsius
    
    except ValueError:
        return Exception
    
assert fahrenheitCelsius(32) == 0
assert fahrenheitCelsius('a') == Exception
assert fahrenheitCelsius(212) == 100
assert fahrenheitCelsius('') == Exception

print('TESTES - ok')
        