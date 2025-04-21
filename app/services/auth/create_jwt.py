from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.constants import ALGORITHM, EXP_TIME, SECRET_KEY

def createJwt(id: str | int) -> str:
  ''' função para gerar e retornar o token JWT '''
  exp = datetime.now(timezone.utc) + timedelta(**EXP_TIME)
  payload = { 'sub': str(id), 'exp': exp }
  token_jwt: str = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
  return token_jwt