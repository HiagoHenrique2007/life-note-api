''' Rotas da entidade Record '''
from fastapi import APIRouter, Depends
from app.schemas.record import Record, RecordUpdate
from app.services.auth.authenticate import getUserId

router = APIRouter(prefix='/record')

@router.get('/')
async def getAllRecords(user_id: int = Depends(getUserId)):
  ''' obter os registro do usuario
    adicionar paginação posteriormente
  '''


@router.get('/emotions')
async def emotions(user_id: int = Depends(getUserId)) -> list:
  ''' obter quais emoções o cliente ja registrou no banco '''


@router.get('/emotions/by')
async def recordByEmotion(by: str = None, user_id: int = Depends(getUserId)) -> list[dict]:
  ''' buscar os registro filtrando por emoção '''


@router.get('/feeling/by')
async def recordByFeeling(by: str = None, user_id: int = Depends(getUserId)) -> list[dict]:
  ''' buscar os registros no banco filtrando os sentimentos pelo parametro da consulta by '''


# POST e PUT
@router.post('/', status_code=201)
async def registerNewRecord(record: Record, user_id: int = Depends(getUserId)):
  ''' regista um novo registro no banco '''
  # tenho que verificar se ja nao existe esse registro no banco
  feeling = record.feeling
  emotion = record.emotion
  text = record.text

@router.put('/{record_id}', status_code=200)
async def updateRecord(record_id: int, record: RecordUpdate, user_id: int = Depends(getUserId)):
  ''' atualizar um registro '''



