from datetime import datetime, timedelta, timezone
from jose import jwt
from app.config import ALGORITHM, SECRET_KEY

async def generate_jwt(id: int) -> str:
  ''' função para gerar e retornar o token JWT '''
  exp = datetime.now(timezone.utc) + timedelta(weeks=2)
  payload = {
    'sub': id,
    'exp': exp
  }
  token: str = jwt.encode(payload, SECRET_KEY, ALGORITHM)
  return token