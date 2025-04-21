from app.db.tables import Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from functools import wraps

engine = create_engine('sqlite:///app/database/feeling.db')
Base.metadata.create_all(engine)

def connect(func):
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
