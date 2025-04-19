from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError

SECRET_KEY = b'fIsH-_-BaLLCAT20comer70correr'
ALGORITIHM = 'HS256'

''' o OAuthPasswordBearer é uma dependencia pronta que me retorna o token ja separado do header
  o primeiro parametro diz para o fastapi onde o usuario pode obter o token JWT
 '''
oauth2_schema = OAuth2PasswordBearer('login')

async def getCustomerId(token: str = Depends(oauth2_schema)):
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITIHM)
    customer_id =  payload.get('sub', None)
    if customer_id is None:
      raise HTTPException(401, 'Token Invalido: claim sub ausente!')
    return customer_id
  
  except ExpiredSignatureError: # exceção se o token estiver expirado
    raise HTTPException(401, detail='Token Expirado!')
  except JWTError: # exceção se o token foi auterado e quebrou a signature
    print('Token Adulterado!\tDanger!!!')