from datetime import datetime
from sqlalchemy import (
  Integer,
  String,
  DateTime 
)
from sqlalchemy.orm import (
  DeclarativeBase, # classe para criar uma tabela
  Mapped, # define os type hints
  mapped_column, # cria a coluna
  relationship, # define as relações entre os campos das tabelas
)

''' isso é necessario para que todas as tabelas sejam centralizadas em uma Base
  pois o DeclarativeBase cria um contexto separado para cada tabela 
'''
class Base(DeclarativeBase): pass

# mixin
class CreatedUpdatedAt:
  created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
  updated_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow
  )

# tabelas
class User(Base):
  __tablename__ = 'user'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False)
  password: Mapped[str] = mapped_column(String, nullable=False)

  def __repr__(self):
    return f'User: ID: {self.id}, NAME: {self.name}, EMAIL: {self.email}'
  
class Record(Base, CreatedUpdatedAt):
  __tablename__ = 'record'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  customer_id: Mapped[int] = mapped_column(Integer, nullable=False)
  feeling: Mapped[str] = mapped_column(String, nullable=False)
  emotion: Mapped[str] = mapped_column(String, nullable=False)
  text: Mapped[str] = mapped_column(String, nullable=False)