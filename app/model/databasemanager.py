from sqlalchemy import (
  Integer,
  String,
)
from sqlalchemy.orm import (
  DeclarativeBase, # classe para criar uma tabela
  Mapped, # define os type hints
  mapped_column, # cria a coluna
  relationship # define as relações entre os campos das tabelas
)

''' isso é necessario para que todas as tabelas sejam centralizadas em uma Base
  pois o DeclarativeBase cria um contexto separado para cada tabela 
'''
class Base(DeclarativeBase): pass

# tabelas
class Customer(Base):
  __tablename__ = 'customer'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False)
  password: Mapped[str] = mapped_column(String, nullable=False)

  def __repr__(self):
    return f'Customer:  id: {self.id}  -  name: {self.name}  -  email: {self.email}'
  
class record(Base):
  __tablename__ = 'record'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)