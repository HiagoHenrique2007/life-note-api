from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError, ExpiredSignatureError


''' o OAuthPasswordBearer é uma dependencia pronta que me retorna o token ja separado do header
  o primeiro parametro diz para o fastapi onde o usuario pode obter o token JWT
 '''
oauth2_schema = OAuth2PasswordBearer('login')

async def getCustomerId(token: str = Depends(oauth2_schema)):
  try:
    payload = jwt.decode(token, )

  except ExpiredSignatureError:
    HTTPException(401, detail='Token Expirado!')
  except JWTError:
    print('Token Adulterado!\tDanger!!!')