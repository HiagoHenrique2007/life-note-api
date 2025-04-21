''' Rotas da entidade User '''
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import SignupData
from app.services.auth.authenticate import getUserId
from app.services.auth.create_jwt import createJwt
from app.services.password import createPwdHash, checkPwdHash
from app.services.model.db_model import db_model


router = APIRouter(prefix='/customer')

# obter as informações basicas do customer
@router.get('/info')
async def customerInfo(id: int = Depends(getUserId)):
  ''' buscar os dados do usuario como email e nome e enviar para o front e salvar no localStorage ''' 

# login
'''OAuthPasswordRequestForm é o password flow do OAuth 2.0
 onde os dados de autenticação do usuario são username e password,
 e essa dependencia do fastapi faz o trabalho de pegar os campos do form
'''
@router.post('/login')
async def login(login_data: OAuth2PasswordRequestForm = Depends()): 
  email = login_data.username
  password = login_data.password
  if email is None or password is None:
    raise HTTPException(401, detail='Username ou password ausentes!')
  # ver se a porra do cara ta no banco
  if not db_model.dontHasEmailOnDb(email=email):
    user = db_model.getCustomerInfo(email=email)
  if not checkPwdHash(password, user.password):
    raise HTTPException(401, 'Senha invalida!')
  token = createJwt(user.id)
  return  {"access_token": token, "token_type": "bearer"}

# criar conta se nao tiver
@router.post('/signup', status_code=201)
async def createAccount(signup_data: SignupData):
  # pendencia: verificar se o email ja esta cadastrado
  email = signup_data.email
  name = signup_data.name
  password = signup_data.password
  pwd_hash = createPwdHash(password)
