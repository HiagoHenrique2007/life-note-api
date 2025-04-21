from fastapi import HTTPException
from app.database.tables import Base, Customer, Record
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from functools import wraps

engine = create_engine('sqlite:///app/database/feeling.db')
Base.metadata.create_all(engine)

def createSession(func):
  print(f'Func: {func}') # executa somente essa parte
  @wraps(func)
  def wrapper(self, *args, **kwargs):
    print(f'ARGS: {args}\n')
    print(f'KWARGS: {kwargs}\n')
    with Session(bind=engine) as session:
      print(f'SESSION: {session}')
      print(f'EXECUTANDO A FUNC')
      result = func(self, *args, session=session, **kwargs)
    return result
  return wrapper

class Model:
  def __init__(self): pass

  @createSession
  def createCustomer(self, *, name: str, email: str, password: str, session: Session):
    print(f'SESSION DENTRO DA FUNC: {session}')
    if not self.dontHasEmailOnDb(email=email, session=session): # se nao tiver o email vai retornar True, entao eu passo para False, que vai significar que ja existe usuario
      raise HTTPException(409, detail='Usuario ja cadastrado!')
    customer = Customer(name=name, email=email, password=password)
    session.add(customer)
    session.commit()
    
  def dontHasEmailOnDb(self, email: str, session: Session) -> bool:
    stmt = select(Customer.email).where(Customer.email == email)
    result = session.execute(stmt).scalars().first()
    return result is None # eu estou verificando se nao tem o email, entao se o result for None, quer dizer que nao tem o email no banco, 

  @createSession
  def getCustomerInfo(self, *, session: Session, email: str) -> Customer:
    stmt = select(Customer).where(Customer.email == email)
    customer = session.scalars(stmt).all()
    return customer[0]


model = Model()
