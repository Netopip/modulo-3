from fastapi import FastAPI,HTTPException,status
from fastapi.routing import APIRouter
from rotas.rotas_task import route_task
from rotas.rotas_autenticacao import routs_autenticacao



app = FastAPI()

app.include_router(route_task)

app.include_router(routs_autenticacao)