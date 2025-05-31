from fastapi import APIRouter,HTTPException,status
from daos.autenticacaoDAO import AutenticacaoDAO
from modelos.model import SingUp,Singin
from utilitarios.utilitarios import hash_password,verificar_hash_password,criar_toke_acesso

autenticacaoDAO = AutenticacaoDAO()

routs_autenticacao = APIRouter()

@routs_autenticacao.post('/auth/singup',status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario:SingUp):
    usuario_existente_email = autenticacaoDAO.buscar_usuario_email(usuario.email)
    usuario_existente_username = autenticacaoDAO.buscar_usuario_username(usuario.username)
    
    if usuario_existente_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Usuário já cadastrado com email {usuario.email}')
    if usuario_existente_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'Usuario ja cadastrado com username {usuario.username}')
    
    usuario.password_hash = hash_password(usuario.password_hash)
    usuario = autenticacaoDAO.salvar_usuario(usuario)
    
    return usuario

@routs_autenticacao.post('/auth/singin',status_code=status.HTTP_200_OK)
def login(usuario:Singin):
    usuario_existente = autenticacaoDAO.buscar_usuario_email(usuario.email)
    
    if not usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail=f'Email e/ou senha incorreto(s)!')
  
    if not verificar_hash_password(usuario.password_hash, usuario_existente.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                        detail=f'Email e/ou senha incorreto(s)!')
        
    token_acesso = criar_toke_acesso(usuario_existente.email)  
    
  
    return {
    'username': usuario_existente.username,
    'access_token': token_acesso}
    

