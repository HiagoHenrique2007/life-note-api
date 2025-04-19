from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.utils.customer_id import getCustomerId

class By(BaseModel):
  by: str

record_router = APIRouter(prefix='/record')

@record_router.get('/')
async def getAllRecords(customer_id: int = Depends(getCustomerId)):
  pass

@record_router.get('/by/emotion')
async def recordByEmotion(
    by: By,
    customer_id: int = Depends(getCustomerId)
  ):
  pass

@record_router.get('/by/feeling')
async def recordByFeeling(
    by: By,
    customer_id: int = Depends(getCustomerId)
  ):
  pass