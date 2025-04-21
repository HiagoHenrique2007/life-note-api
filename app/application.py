from fastapi import FastAPI
from app.routes import customer, record, text
from app.routes import record, user

app = FastAPI()
app.include_router(customer.customer_router)
app.include_router(record.record_router)
app.include_router(text.text_router)
