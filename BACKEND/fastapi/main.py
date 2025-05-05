from fastapi import FastAPI    
from veiculos_routes import roteador_veiculos
from auth_routes import router as roteador_auth
from montadoras_routes import app as roteador_montadoras
                   


app = FastAPI()

#rotas veiculos 
app.include_router(roteador_veiculos)

#rotas Autenticação
app.include_router(roteador_auth)

#Rotas Montadoras
app.include_router(roteador_montadoras)