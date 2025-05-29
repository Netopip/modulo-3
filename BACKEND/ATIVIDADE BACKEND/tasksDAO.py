import sqlite3
from model import Usuario,Task,TaskCreate

class TaskDAO:
    def __init__(self):
        pass
    
    def criar_task(self,user:Usuario,task:TaskCreate):
        with sqlite3.connect('banco.db') as connect:
            cursor = connect.cursor()
            query = 'insert into tarefa(titulo,descricao,concluida,usuario_id) values (?,?,?,?)'
            cursor.execute(query,(task.titulo,task.descricao,task.concluida,user.id))
            
            id = cursor.lastrowid
            
            return Task(id=id,usuario_id=user.id,**task.dict())
     
     
    def listar_tasks(self,user:Usuario):
        with sqlite3.connect('banco.db') as con:
            cursor = con.cursor()
            query = 'select * from tarefa where usuario_id =?'
            cursor.execute(query,(user.id,))
            
            resultado = cursor.fetchall()
            
            tasks: list[Task] = []
            
            for linha in resultado:
                task = Task(id=linha[0],
                            titulo=linha[1],
                            descricao=linha[2],
                            concluida=linha[3],
                            usuario_id=linha[4])
                
                tasks.append(task)
            return tasks
        
    def listar_task_id(self,user:Usuario,id:int):
        with sqlite3.connect('banco.db') as con:
            cursor = con.cursor()
            query = 'select * from tarefa where usuario_id=? and id=?'
            cursor.execute(query,(user.id,id))
            
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
            
            task = Task(id=resultado[0],
                        titulo=resultado[1],
                        descricao=resultado[2],
                        concluida = resultado[3],
                        usuario_id=resultado[4])
            return task
        
        
    def excluir_task(self,user:Usuario,id:int):
        with sqlite3.connect('banco.db') as con:
            cursor = con.cursor()
            query = 'delete from tarefa where usuario_id=? and id=?'
            cursor.execute(query,(user.id,id))
            
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
            
            
    def atualizar_tarefa(self,task:Task,user:Usuario,id:int):
        with sqlite3.connect('banco.db') as cone:
            cursor = cone.cursor()
            query = 'UPDATE tarefa set titulo=?, descricao=?, concluida=? where id =? and usuario_id=?'
            cursor.execute(query,(task.titulo,task.descricao,task.concluida,id,user.id))
            
            return Task(id=id,usuario_id=user.id,**task.dict())
            
            
           
        
    
            
            