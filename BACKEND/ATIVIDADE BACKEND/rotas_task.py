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
    return tasks