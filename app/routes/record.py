from fastapi import APIRouter, Depends
from app.utils import customer_id
from app.utils.customer_id import getCustomerId
from pydantic import BaseModel

# record model
class Record(BaseModel):
  feeling: str
  emotion: str
  text: str

class RecordUpdate(BaseModel):
  feeling: str | None = None
  emotion: str | None = None
  text: str | None = None

record_router = APIRouter(prefix='/record')

@record_router.get('/')
async def getAllRecords(customer_id: int = Depends(getCustomerId)):
  ''' obter os registro do usuario
    adicionar paginação posteriormente
  '''


@record_router.get('/emotions')
async def emotions(customer_id: int = Depends(getCustomerId)) -> list:
  ''' obter quais emoções o cliente ja registrou no banco '''


@record_router.get('/emotions/by')
async def recordByEmotion(by: str = None, customer_id: int = Depends(getCustomerId)) -> list[dict]:
  ''' buscar os registro filtrando por emoção '''


@record_router.get('/feeling/by')
async def recordByFeeling(by: str = None, customer_id: int = Depends(getCustomerId)) -> list[dict]:
  ''' buscar os registros no banco filtrando os sentimentos pelo parametro da consulta by '''


# POST e PUT
@record_router.post('/', status_code=201)
async def registerNewRecord(record: Record, customer_id: int = Depends(getCustomerId)):
  ''' regista um novo registro no banco '''
  # tenho que verificar se ja nao existe esse registro no banco
  feeling = record.feeling
  emotion = record.emotion
  text = record.text

@record_router.put('/{record_id}', status_code=200)
async def updateRecord(record_id: int, record: RecordUpdate, customer_id: int = Depends(getCustomerId)):
  ''' atualizar um registro '''



