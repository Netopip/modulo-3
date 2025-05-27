from fastapi import FastAPI, HTTPException,status
from modelosclasse import ClienteCreate
from clientedao import ClienteDAO

app = FastAPI()

clientedao = ClienteDAO()
    
@app.post('/cliente',status_code=status.HTTP_201_CREATED)
def adicionar_cliente(cliente:ClienteCreate):
    novo = clientedao.criar_cliente(cliente)
    return novo

@app.get('/listar_clientes',status_code=status.HTTP_200_OK)
def Listar_todos():
    clientes = clientedao.listar_clientes()
    return clientes
    
@app.get('/listar_clientes_por_id/{id}',status_code=status.HTTP_200_OK)
def listar_por_id(id:int):
    cliente = clientedao.listar_por_id(id)
    
    if cliente:
        return cliente
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Cliente não encontrado')
    
@app.delete('/deletar_cliente/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletar_cliente(id:int):
    if listar_por_id(id):
        clientedao.deletar_cliente(id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Cliente nao encontrado!')
    
    
@app.put('/atualizar_cliente/{id}',status_code=status.HTTP_200_OK)
def atualizar_cliente(id:int,cliente:ClienteCreate):
    cliente_atual = clientedao.atualizar_cliente(id,cliente)
    if listar_por_id(id):
        return cliente_atual
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Cliente não encontrado!')
    

