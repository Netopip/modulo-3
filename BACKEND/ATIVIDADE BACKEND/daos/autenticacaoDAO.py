import sqlite3
from modelos.model import Usuario,SingUp

class AutenticacaoDAO:
    def __init__(self):
        pass
    
    def buscar_usuario_email(self,email:str):
        with sqlite3.connect('banco.db') as conec:
            cursor = conec.cursor()
            query = 'select * from usuario where email = ?'
            cursor.execute(query,(email,))
            
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
            
            usuario = Usuario(id=resultado[0],
                              username=resultado[1],
                              email = resultado[2],
                              password_hash=resultado[3])
            return usuario
        
        
    def buscar_usuario_username(self,username:str):
        with sqlite3.connect('banco.db') as conec:
            cursor = conec.cursor()
            query = 'select * from usuario where username = ?'
            cursor.execute(query,(username,))
            
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
            
            usuario = Usuario(id=resultado[0],
                              username=resultado[1],
                              email = resultado[2],
                              password_hash=resultado[3])
            return usuario
        
    
    def salvar_usuario(self,usuario:SingUp):
        with sqlite3.connect('banco.db') as conect:
            cursor = conect.cursor()
            query = '''INSERT INTO usuario(username, email, password_hash )
              VALUES (?, ?, ? )'''
      
            cursor.execute(query, (usuario.username, usuario.email, usuario.password_hash))

            id = cursor.lastrowid

            return Usuario(id=id, **usuario.dict())
        
    
  
        
        
        