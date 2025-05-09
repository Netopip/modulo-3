from random import *

def listaComCemElementos():
    
    elementos = [randint(-100,100) for i in range(100)]
    return elementos

print(listaComCemElementos())