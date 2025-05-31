from fastapi import APIRouter,HTTPException,status,Depends
from model import Usuario,Task,TaskCreate
from typing import Annotated
from utilitarios import get_current_user
from tasksDAO import TaskDAO

taskDAO = TaskDAO()

route_task = APIRouter()

@route_task.post('/tarefas',status_code=status.HTTP_201_CREATED)
def criar_task(novo:TaskCreate,user:Annotated[Usuario,Depends(get_current_user)]):
    task = taskDAO.criar_task(user,novo)
    return task

@route_task.get('/listartarefas',status_code=status.HTTP_200_OK)
def listar_tasks(user:Annotated[Usuario,Depends(get_current_user)]):
    tasks = taskDAO.listar_tasks(user)
    if tasks:   
        return tasks
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='nenhuma task encontrada')

@route_task.get('/listartarefas/{id}',status_code=status.HTTP_200_OK)
def listar_tarefa_id(user:Annotated[Usuario,Depends(get_current_user)],id:int):
    tarefa = taskDAO.listar_task_id(user,id)
    
    if tarefa:
        return tarefa
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Não autorizado')

@route_task.delete('/deletartarefa/{id}',status_code=status.HTTP_204_NO_CONTENT)
def deletar_task(user:Annotated[Usuario,Depends(get_current_user)],id:int):
    if listar_tarefa_id(user,id):
        taskDAO.excluir_task(user,id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='task não encontrada')
    
    
@route_task.put('/atualizartarefa/{id}',status_code=status.HTTP_200_OK)
def atualizar_tarefa(user:Annotated[Usuario,Depends(get_current_user)],id:int,task:TaskCreate):
    if listar_tarefa_id(user,id):
        return taskDAO.atualizar_tarefa(task,user,id)
        

    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Não autorizado')

@route_task.get('/me',status_code=status.HTTP_200_OK)
def exibir_me(user:Annotated[Usuario,Depends(get_current_user)]):
    return {
        'Username':user.username,
        'Email': user.email,
        'Id': user.id        
    }
