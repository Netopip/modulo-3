
def adicionar_lista(lista):
    lista_nova = []
    ultimo_termo = 0
    for i in lista:
        lista_nova.append(i)
        ultimo_termo += i
    lista_nova.append(ultimo_termo)
    
    return lista_nova
    
    
def main():
    lista = []
    
    while True:
        try:
            num = int(input().strip())
            if num == 0:
                break
            else:
                lista.append(num)
        
        except ValueError:
            print("Valor inválido. Tente novamente.")
            
    print(lista)
    print(adicionar_lista(lista))
    

if __name__ == "__main__":
    main()