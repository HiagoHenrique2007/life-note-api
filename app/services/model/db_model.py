''' manipulador e concentrador de logica de banco '''
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db.connection import connect
from app.db.tables import Record, User

class DbModel:
  @connect
  def createUser(self, *, name: str, email: str, password: str, session: Session):
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    
  @connect
  def dontHasUser(self, *, email: str, session: Session) -> bool:
    stmt = select(User.email).where(User.email == email)
    result = session.execute(stmt).scalars().first()
    # eu estou verificando se nao tem o email, entao se o result for None, quer dizer que nao tem o email no banco e vai retornar True 
    return result is None

  @connect
  def userInfo(self, id: int = None, email: str = None,  session: Session = None) -> User:
    if id is not None:
      stmt = select(User).where(User.id == id)
    else:
      stmt = select(User).where(User.email == email)
    user = session.scalars(stmt).all()
    return user[0]

db_model = DbModel()
