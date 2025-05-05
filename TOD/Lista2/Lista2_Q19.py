from random import * 

def main():
    lista_r = [randint(1,100) for i in range(5)]
    lista_s = [randint(1,100) for i in range(10)]
    
    lista_mod = []
    for i in range(len(lista_r)):
        lista_mod.append(lista_r[i])
    for i in range(len(lista_s)):
        lista_mod.append(lista_s[i])
    
    print("Lista R: ", lista_r)
    print("Lista S: ", lista_s)
    print("Lista Modificada: ", lista_mod)

if __name__ == "__main__":
    main()
    