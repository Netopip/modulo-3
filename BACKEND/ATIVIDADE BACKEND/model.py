from pydantic import BaseModel


class UsuarioBase(BaseModel):
    username : str
    email : str
    password_hash : str
    
class Usuario(UsuarioBase):
    id : int | None = None

#tarefas

class TaskfasBase(BaseModel):
    titulo: str
    descricao : str | None = None
    concluida: bool = False
    usuario_id : int
    
class Task(TaskfasBase):
    id : int | None = None
    
class TaskCreate(TaskfasBase):
    ...
    
    
class Singin(BaseModel):    
    email :str
    password_hash :str
    
class SingUp(UsuarioBase):
    pass