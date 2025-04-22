''' Rotas da entidade User '''
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.services.auth.authenticate import getUserId
from app.schemas.user import SignupData
from app.services.auth.create_jwt import createJwt
from app.services.password import createPwdHash, checkPwdHash
from app.services.model.db_model import db_model
from app.core.constants import EXP_TIME


router = APIRouter(prefix='/customer')

# obter as informações basicas do customer
@router.get('/info')
async def customerInfo(id: int = Depends(getUserId)):
  ''' buscar os dados do usuario como email e nome e enviar para o front e salvar no localStorage ''' 
  user = db_model.userInfo(id=id)
  return { 'id': user.id, 'name': user.name, 'email': user.email }

# login
'''OAuthPasswordRequestForm é o password flow do OAuth 2.0
 onde os dados de autenticação do usuario são username e password,
 e essa dependencia do fastapi faz o trabalho de pegar os campos do form
'''
@router.post('/login')
async def login(response: Response, login_data: OAuth2PasswordRequestForm = Depends()): 
  email = login_data.username
  password = login_data.password
  if email is None or password is None:
    raise HTTPException(401, detail='Username ou password ausentes!')
  # ver se a porra do cara ta no banco
  if not db_model.dontHasUser(email=email):
    user = db_model.userInfo(email=email)
  else:
    raise HTTPException(401, 'Email invalido!')
  if not checkPwdHash(password, user.password):
    raise HTTPException(401, 'Senha invalida!')
  token_jwt = createJwt(user.id)
  response.set_cookie(
    key='access-token', # nome do cookie
    value=token_jwt, # valor do cookie
    max_age=timedelta(**EXP_TIME), # quando o cookie ficar invalido
    httponly=True, # acessado apenas com requisição
    samesite='strict' # é enviado somente pela origem que gerou ele
  )
  return  { 'loged': True }

# criar conta se nao tiver
@router.post('/signup', status_code=201)
async def createAccount(signup_data: SignupData, response: Response):
  email = signup_data.email
  if  db_model.dontHasUser(email=email):
    name = signup_data.name
    password = signup_data.password
    pwd_hash = createPwdHash(password)
    db_model.createUser(name=name, email=email, password=pwd_hash)
    user = db_model.userInfo(email=email)
    if user is None:
      raise HTTPException(500, detail='Erro ao criar o usuario!')
    token_jwt = createJwt(user.id)
    response.set_cookie(
      key='access-token', # nome do cookie
      value=token_jwt, # valor do cookie
      max_age=timedelta(**EXP_TIME), # quando o cookie ficar invalido
      httponly=True, # acessado apenas com requisição
      samesite='strict' # é enviado somente pela origem que gerou ele
    )
    return { 'message': 'Usuario criado' }
  else:
    raise HTTPException(409, 'Usuario ja cadastrado!')
