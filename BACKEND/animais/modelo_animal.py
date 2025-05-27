from pydantic import BaseModel

class AnimalBase(BaseModel):
    nome : str
    idade : int
    sexo : str
    especie : str
    cor : str
    
class Animal(AnimalBase):
    id : int | None = None
    

class AnimalCreate(AnimalBase):
    pass