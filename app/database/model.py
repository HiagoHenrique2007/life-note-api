from fastapi import HTTPException
from app.database.tables import Base, Customer, Record
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from functools import wraps

def createSession(func):
  @wraps(func)
  def wrapper(self, *args, **kwargs):
    with Session(self.engine) as session:
      return func(self, *args, session=session, **kwargs)
  return wrapper

class Model:
  def __init__(self):
    self.engine = create_engine('sqlite:///app/database/feeling.db')
    Base.metadata.create_all(self.engine)

  @createSession
  def createCustomer(self, *, name: str, email: str, password: str, session: Session = None):
    if not self.dontHasEmailOnDb(email): # se nao tiver o email vai retornar True, entao eu passo para False, que vai significar que ja existe usuario
      raise HTTPException(409, detail='Usuario ja cadastrado!')
    customer = Customer(name=name, email=email, password=password)
    session.add(customer)
    session.commit()
    
  def dontHasEmailOnDb(self, email: str) -> bool:
    with Session(self.engine) as session:
      stmt = select(Customer.email).where(Customer.email == email)
      result = session.execute(stmt).scalars().first()
      return result is None # eu estou verificando se nao tem o email, entao se o result for None, quer dizer que nao tem o email no banco, 

  def getCustomerInfo(self, email: str, session: Session = None) -> Customer:
    stmt = select(Customer).where(Customer.email == email)
    customer = session.scalars(stmt).all()
    return customer[0]


model = Model()
