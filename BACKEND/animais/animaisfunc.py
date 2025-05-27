from modelo_animal import Animal,AnimalCreate
import sqlite3


class Animalfunc:
    def __init__(self):
        pass
    
    def criar_animal(self,animal: AnimalCreate):
        with sqlite3.connect('animais.db') as connect:
            cursor = connect.cursor()
            query = 'insert into animal(nome,idade,sexo,especie,cor) values (?,?,?,?,?)'
            cursor.execute(query,(
                animal.nome,
                animal.idade,
                animal.sexo,
                animal.especie,
                animal.cor
            ))
            id = cursor.lastrowid
            
            return Animal(id=id,**animal.dict())
        
    def listar_todos(self):
        with sqlite3.connect('animais.db') as con:
            cursor = con.cursor()
            query = 'select * from animal'
            cursor.execute(query)
            
            animais_list = cursor.fetchall()
            animais = []
            
            for linha in animais_list:
                animal = Animal(id=linha[0],
                                nome=linha[1],
                                idade=linha[2],
                                sexo=linha[3],
                                especie=linha[4],
                                cor = linha[5])
                animais.append(animal)
                
            return animais
        
    def listar_por_id(self,id:int):
        with sqlite3.connect('animais.db') as cone:
            cursor = cone.cursor()
            query = 'select * from animal where id=?'
            cursor.execute(query,(id,))
            
            resultado = cursor.fetchone()
            
            if not resultado:
                return None
        
            animal = Animal(id=resultado[0],
                            nome = resultado[1],
                            idade=resultado[2],
                            sexo = resultado[3],
                            especie=resultado[4],
                            cor = resultado[5])
            return animal
    
    
    def deletar_animal(self,id:int):
        with sqlite3.connect('animais.db') as c:
            cursor = c.cursor()
            query = 'delete from animal where id=?'
            cursor.execute(query,(id,))
            result = cursor.fetchone()
            
            if not result:
                return None
            
    
    def atualizar_animal(self,id:int,animal:Animal):
        with sqlite3.connect('animais.db') as con:
            cursor = con.cursor()
            query = 'update animal set nome=?,idade=?,sexo=?,especie=?,cor=? where id=?'
            cursor.execute(query,(animal.nome,
                                  animal.idade,
                                  animal.sexo,
                                  animal.especie,
                                  animal.cor,
                                  id))
            
            return Animal(id=id,**animal.dict())