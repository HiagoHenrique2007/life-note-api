from app.db.tables import Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from functools import wraps

engine = create_engine('sqlite:///app/db/feeling.db')
Base.metadata.create_all(engine)

def connect(func):
  @wraps(func)
  def wrapper(self, *args, **kwargs):
    with Session(bind=engine) as session:
      result = func(self, *args, **kwargs, session=session)
    return result
  return wrapper
