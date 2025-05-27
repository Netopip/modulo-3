from datetime import datetime, timezone, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext

from autenticacaoDAO import AutenticacaoDAO

autenticacaoDAO = AutenticacaoDAO()



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str):
    hash = pwd_context.hash(password)
    return hash

def verificar_hash_password(password:str, hash_password: str):
    return pwd_context.verify(password,hash_password)


SECRET_KEY = "USER"
ALGORITHM = "HS256"

def criar_toke_acesso(email:str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    data = {
        'sub': email,
        'exp': expire
    }
    token = jwt.encode(data, SECRET_KEY,ALGORITHM)
    
    return token

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: Annotated[str,Depends(oauth_scheme)]):
    try:
        data = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email = data['sub']
        user = autenticacaoDAO.buscar_usuario_email(email)
        return user
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='token inválido')