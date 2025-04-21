from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.utils.customer_id import getCustomerId
from app.utils.pwd import checkPwd, generatePwdHash
from app.utils.jwtencode import generateJwt
from app.database.model import model

class SignupData(BaseModel):
  name: str
  email: str
  password: str

customer_router = APIRouter(prefix='/customer')

@customer_router.get('/')
async def getUsers():
  return 1

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
  # ver se a porra do cara ta no banco
  if not model.dontHasEmailOnDb(email=email):
    customer = model.getCustomerInfo(email=email)
  if not checkPwd(password, customer.password):
    raise HTTPException(401, 'Senha invalida!')
  token = generateJwt(customer.id)
  return  {"access_token": token, "token_type": "bearer"}

# criar conta se nao tiver
@customer_router.post('/signup', status_code=201)
async def createAccount(signup_data: SignupData):
  # pendencia: verificar se o email ja esta cadastrado
  email = signup_data.email

  name = signup_data.name
  password = signup_data.password
  pwd_hash = generatePwdHash(password)
  user = {
    'id': 1,
    'name': name,
    'email': email,
    'hash': pwd_hash
  }
