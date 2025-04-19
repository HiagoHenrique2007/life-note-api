from fastapi import FastAPI, Depends
from sqlalchemy import create_engine

app = FastAPI()

@app.get('/records')
async def records(userId: int = Depends()):
  pass


@app.get('/record/by/emotion')
async def recordByEmotion():
  pass

@app.get('/record/by/feeling')
async def recordByFeeling():
  pass

