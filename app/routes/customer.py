from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.utils.customer_id import getCustomerId
from app.utils.pwd import checkPwd, generatePwdHash
from app.utils.jwtencode import generateJwt

class SignupData(BaseModel):
  name: str
  email: str
  password: str

customer_router = APIRouter(prefix='/customer')

@customer_router.get('/info')
async def customerInfo(id: int = Depends(getCustomerId)):
  ''' buscar os dados do usuario como email e nome e enviar para o front ''' 

@customer_router.post('login')
async def login(login_data: OAuth2PasswordRequestForm = Depends()):
  username = login_data.username
  password = login_data.password
  id = None # tenho que implementar a parte do banco, nao ta pronta ainda
  if username is None or password is None:
    raise HTTPException(401, detail='Username ou password ausentes!')
  if not await checkPwd(id, password):
    raise HTTPException(401, 'Senha invalida!')
  token = await generateJwt(id)

@customer_router.post('/signup')
async def createAccount(signup_data: SignupData):
  name = signup_data.name
  email = signup_data.email
  password = signup_data.password
  pwd_hash = generatePwdHash(password)
