def mostrar_menu():
    return '1 - Cadastrar cliente\n2 - Pesquisar cliente\n3 - Mostrar lista de clientes\n4 - Alterar cliente\n5 - Excluir cliente \n0 - Sair\n'


  
def cadastrar_cliente():
    while True:
        nome = input('Digite o nome do cliente:\n').strip()
        if nome == '':
            print('Nome inválido!')
            continue
        else:
            break
    return nome

def pesquisar_cliente(lista_nomes):
    while True:
        nome_cliente = input('Digite o nome do cliente a ser pesquaisado:\n').strip()
        if nome_cliente == '':
            print('Nome inválido!')
            continue
        else:
            break
        
    for indice,nome in enumerate(lista_nomes):
        if nome_cliente == nome:
            print(f'Cliente {nome_cliente} encontrado na posição {indice}!')
            return
            
    print(f'Cliente {nome_cliente} não encontrado!')
    
def mostrar_clientes(clientes):
    print('Lista de clientes:')
    for i in clientes:
        print(i)
        
        
def alterar_cliente(clientes):
    while True:
        nome_cliente_alterar = input('Digite o nome do cliente que deseja alterar:\n').strip()
        if nome_cliente_alterar == '':
            print('Digite um nome!')
            continue
        else:
            break
        
    for i,j in enumerate(clientes):
        if nome_cliente_alterar == j:
            while True:
                novo_nome = input('Digite o novo nome:\n').strip()
                if novo_nome == '':
                    print('Digite um nome válido!')
                    continue
                else:
                    clientes[i] = novo_nome
                    print(f'Cliente {nome_cliente_alterar} alterado para {novo_nome}!')
                    return
    
    print(f'Cliente de nome {nome_cliente_alterar} não encontrado!')
    

         
               
def excluir_cliente(clientes):
    nova_lista = []
    while True:
        nome_cliente_excluir = input('Digite o nome do cliente para excluir:\n').strip()
        if nome_cliente_excluir == '':
            print('Digite um nome!')
            continue
        else:
            break
    ask = input(f'Você tem certeza que deseja excluir o cliente {nome_cliente_excluir}?\nDigite S para sim ou N para não:\n').strip().upper()
    if ask != 'S':
        print('Exclusão cancelada!')
        return
        
    for i,j in enumerate(clientes):
        if nome_cliente_excluir != j:
             nova_lista.append(j)
    print(f'Cliente {nome_cliente_excluir}  da posição {i} excluído com sucesso!')
        
    clientes[:] = nova_lista
    
    
        

def main():
    clientes = []
    
    while True:
        opcao = input(f'{mostrar_menu()}\nEscolha uma opção: ').strip()
        if opcao == '1':
            cliente = cadastrar_cliente()
            clientes.append(cliente)
            print(f'Cliente {cliente} cadastrado com sucesso!\n')
            
        elif opcao == '2':
            if clientes:
                pesquisar_cliente(clientes)
            else:
                print('Nenhum cliente cadastrado!')
            
        elif opcao == '3':
            if clientes:
                mostrar_clientes(clientes)
            else:
                print('Nenhum cliente cadastrado!')
                
        elif opcao == '4':
            if clientes:
                alterar_cliente(clientes)
            else:
                print('Nenhum cliente cadastrado!')
                
        elif opcao == '5':
            if clientes:
                excluir_cliente(clientes)
            else:
                print('Nenhum cliente cadastrado!')
                
        elif opcao == '0':
            print('Saindo...')
            break
        
        else:
            print('Opção inválida! Tente novamente.')
            
    
if __name__ == "__main__":
    main()