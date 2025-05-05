from random import *


max_lista = 10

def main():
    lista_x =[randint(1,100) for _ in range(max_lista)]
    lista_y = []
    for i in range(len(lista_x)):
        if i%2==0:
            lista_y.append(lista_x[i] /2)
        else:
            lista_y.append(lista_x[i]*3)
    
    print(lista_x)
    print(lista_y)
    
if __name__ == "__main__":
    main()
        