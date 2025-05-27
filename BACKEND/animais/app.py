from fastapi import FastAPI, HTTPException,status

from animaisfunc import Animalfunc
from modelo_animal import Animal,AnimalCreate
    

app = FastAPI()
animaisfunc = Animalfunc()

@app.get('/listaranimais',status_code=status.HTTP_200_OK)
def listar_animais():
    animais = animaisfunc.listar_todos()
    return animais

@app.post('/criaranimal',status_code=status.HTTP_201_CREATED)
def criar_animal(animal:AnimalCreate):
    novo_animal = animaisfunc.criar_animal(animal)
    return novo_animal


@app.get('/listaranimais/{id}',status_code=status.HTTP_200_OK)
def listar_animal_id(id:int):
    animal = animaisfunc.listar_por_id(id)
    
    if animal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Aniaml não encontrado')
    return animal
    

@app.delete('/deletaranimal/{id}',status_code=status.HTTP_200_OK)
def deletar_animal(id:int):
    if listar_animal_id(id):
        animaisfunc.deletar_animal(id)
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Animal não encontrado')
    
    
@app.put('/atualizarnimal/{id}',status_code=status.HTTP_200_OK)
def atualizar_animal(id:int,animal:AnimalCreate):
    if listar_animal_id(id):
        animal_atualizado = animaisfunc.atualizar_animal(id,animal)
        return animal_atualizado
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Animal não encontrado')
   
    
    


    
    

