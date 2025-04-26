from datetime import datetime, timezone
from sqlalchemy import (
  Boolean,
  ForeignKey,
  Integer,
  String,
  DateTime,
  Table
)
from sqlalchemy.orm import (
  DeclarativeBase, # classe para criar uma tabela
  Mapped, # define os type hints
  mapped_column, # cria a coluna
  relationship, # define as relações entre os campos das tabelas
)

def set_datetime(): datetime.now(timezone.utc)

# mixins
class CreatedUpdatedAt:
  created_at: Mapped[datetime] = mapped_column(DateTime, default=set_datetime)
  updated_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=set_datetime,
    onupdate=set_datetime
  )

class IdPrimaryKey:
  id: Mapped[int] = mapped_column(Integer, primary_key=True)

class UserId:
  user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)

# tabelas
class Base(DeclarativeBase): pass
''' `class Base(DeclarativeBase): pass` isso é necessario para que todas as tabelas sejam centralizadas em uma Base
  pois o DeclarativeBase cria um contexto separado para cada tabela 
'''

class User(Base, IdPrimaryKey):
  __tablename__ = 'user'

  name: Mapped[str] = mapped_column(String(50), nullable=False)
  email: Mapped[str] = mapped_column(String, nullable=False)
  password: Mapped[str] = mapped_column(String, nullable=False)
  ''' `Mapped[list['record]]` diz que o atributo records sera uma list de Records
    `back_populates='user'` faz com que o SQLAlchemy crie o atributo records
    que tera os records do user quando o user for buscado
   '''
  records: Mapped[list['Record']] = relationship('Record', back_populates='user', lazy='select')

  def __repr__(self):
    return f'User: ID: {self.id}, NAME: {self.name}, EMAIL: {self.email}'
  
class Record(Base, IdPrimaryKey, UserId,  CreatedUpdatedAt):
  __tablename__ = 'record'

  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  emotion_id: Mapped[str] = mapped_column(ForeignKey(''), nullable=False)
  title: Mapped[str] = mapped_column(String, default=None)
  text: Mapped[str] = mapped_column(String, nullable=False)
  favorite: Mapped[bool] = mapped_column(Boolean, default=False)

class Emotion(Base, IdPrimaryKey, UserId, CreatedUpdatedAt):
  emotion_name: Mapped[str] = mapped_column(String, nullable=False)
  color: Mapped[str] = mapped_column(String)