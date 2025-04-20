from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.utils.customer_id import getCustomerId
from app.utils.pwd import checkPwd, generatePwdHash
from app.utils.jwtencode import generateJwt

global users
users = [
  {
    'id': '1',
    'name': 'bebeto',
    'email': 'bebete@bebeto.beto',
    'hash': generatePwdHash('lam007')
  }
]

class SignupData(BaseModel):
  name: str
  email: str
  password: str

customer_router = APIRouter(prefix='/customer')

@customer_router.get('/')
async def getUsers():
  return users

# obter as informações basicas do customer
@customer_router.get('/info')
async def customerInfo(id: int = Depends(getCustomerId)):
  ''' buscar os dados do usuario como email e nome e enviar para o front e salvar no localStorage ''' 

# login
@customer_router.post('/login')
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
  email = login_data.username
  password = login_data.password
  if email is None or password is None:
    raise HTTPException(401, detail='Username ou password ausentes!')
  
  # tenho que implementar a parte do banco, nao ta pronta ainda
  hashed_pwd = None
  id = None
  for user in users:
    if user.get('email') == email:
      id = user.get('id')
      hashed_pwd = user.get('hash')
      print(id, user.get('email'), email, hashed_pwd)
  if hashed_pwd is None: raise HTTPException(400, detail='Email nao cadastrado!')
    
  if not checkPwd(password, hashed_pwd):
    raise HTTPException(401, 'Senha invalida!')
  token = generateJwt(id)
  return  {"access_token": token, "token_type": "bearer"}

# criar conta se nao tiver
@customer_router.post('/signup', status_code=201)
async def createAccount(signup_data: SignupData):
  # pendencia: verificar se o email ja esta cadastrado
  email = signup_data.email
  for user in users:
    if email == user.get('email'):
      raise HTTPException(409, detail='Email ja cadastrado!')
  name = signup_data.name
  password = signup_data.password
  pwd_hash = generatePwdHash(password)
  user = {
    'id': str(int(users[-1].get('id')) + 1),
    'name': name,
    'email': email,
    'hash': pwd_hash
  }
  users.append(user)
  return user
