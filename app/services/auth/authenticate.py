from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError
from app.core.constants import ALGORITHM, SECRET_KEY

''' o OAuthPasswordBearer é uma dependencia pronta que me retorna o token ja separado do header
  o primeiro parametro diz para o fastapi/swagger onde o usuario pode obter o token JWT
 '''
oauth2_schema = OAuth2PasswordBearer(tokenUrl='/customer/login', description='Fazer login!')

def getUserId(token: str = Depends(oauth2_schema)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    print(payload)
    user_id =  payload.get('sub', None)
    if user_id is None:
      raise HTTPException(401, 'Token Invalido: claim sub ausente!')
    return user_id
  
  except ExpiredSignatureError: # exceção se o token estiver expirado
    raise HTTPException(401, detail='Token Expirado!')
  except JWTError: # exceção se o token foi auterado e quebrou a signature
    raise HTTPException(status_code=401, detail='Token Adulterado! Danger!!!')