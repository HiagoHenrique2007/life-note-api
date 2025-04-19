from fastapi import FastAPI
from app.routes import customer, record, text

app = FastAPI()
app.include_router(customer)
app.include_router(record.record_router)
app.include_router(text.text_router)

# @app.get('/records')
# async def records(userId: int = Depends()):
#   pass


# @app.get('/record/by/emotion')
# async def recordByEmotion():
#   pass

# @app.get('/record/by/feeling')
# async def recordByFeeling():
#   pass

