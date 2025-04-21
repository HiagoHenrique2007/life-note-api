from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.constants import ALGORITHM, SECRET_KEY

def createJwt(id: str) -> str:
  ''' função para gerar e retornar o token JWT '''
  exp = datetime.now(timezone.utc) + timedelta(weeks=1)
  payload = { 'sub': id, 'exp': exp }
  token_jwt: str = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
  return token_jwt