from pydantic import BaseModel


class ClienteBase(BaseModel):
    nome: str
    idade: int
   
class  Cliente(ClienteBase):
    id : int | None = None
    
class ClienteCreate(ClienteBase):
    pass