import sqlite3

from modelosclasse import Cliente,ClienteCreate

class ClienteDAO:
    def __init__(self):
        pass
    
    def criar_cliente(self,cliente:ClienteCreate):
        with sqlite3.connect('clientes.db') as conect:
            cursor = conect.cursor()
            query = 'INSERT INTO cliente(nome,idade) VALUES(?,?)'
            
            cursor.execute(query,(cliente.nome,cliente.idade))
            
            id = cursor.lastrowid
            
            return Cliente(id=id,**cliente.dict())
        
    def listar_clientes(self):
        with sqlite3.connect('clientes.db') as con:
            cursor = con.cursor()
            query = 'select * from cliente'
            cursor.execute(query)
            
            clientes_lista = cursor.fetchall()
            clientes = []
            
            for linha in clientes_lista:
                cliente = Cliente(id=linha[0],nome=linha[1],idade=linha[2])
                clientes.append(cliente)
            return clientes
        
    def listar_por_id(self,id:int):
        with sqlite3.connect('clientes.db') as con:
            cursor = con.cursor()
            query = 'select * from cliente where id=?'
            cursor.execute(query,(id,))
            
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
            cliente = Cliente(id=resultado[0],nome=resultado[1],idade=resultado[2])
            return cliente
            
    def deletar_cliente(self,id:int):
        with sqlite3.connect('clientes.db') as con:
            cursor =  con.cursor()
            query = 'delete from cliente where id=?'
            cursor.execute(query,(id,))
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
            
    def atualizar_cliente(self,id:int,cliente:Cliente):
        with sqlite3.connect('clientes.db') as con:
            cursor = con.cursor()
            query = 'UPDATE cliente SET nome=?,idade=? WHERE id=?'
            cursor.execute(query,(cliente.nome,cliente.idade,id))
            
            return Cliente(id=id,**cliente.dict())
