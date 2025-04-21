''' manipulador e concentrador de logica de banco '''
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db import connect
from app.db.tables import Record, User

class DbModel:
  @connect
  def createUser(self, *, name: str, email: str, password: str, session: Session):
    # se nao tiver o email vai retornar True, entao eu passo para False, que vai significar que ja existe usuario
    if not self.dontHasEmailOnDb(email=email, session=session):
      raise HTTPException(409, detail='Usuario ja cadastrado!')
    
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    
  def dontHasUser(self, *, email: str, session: Session) -> bool:
    stmt = select(User.email).where(User.email == email)
    result = session.execute(stmt).scalars().first()
    # eu estou verificando se nao tem o email, entao se o result for None, quer dizer que nao tem o email no banco e vai retornar True 
    return result is None 

  @connect
  def userInfo(self, *, email: str, session: Session) -> User:
    stmt = select(User).where(User.email == email)
    user = session.scalars(stmt).all()
    return user[0]


db_model = DbModel()
