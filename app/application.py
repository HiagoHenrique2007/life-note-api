from fastapi import FastAPI
from app.routes import user, record

app = FastAPI()
app.include_router(user.router)
app.include_router(record.router)
