from fastapi import APIRouter

text_router = APIRouter()

@text_router.get('/text/by/emotion')
async def textByEmotion():
  pass

@text_router.get('/text/by/feeling')
async def textByFeeling():
  pass