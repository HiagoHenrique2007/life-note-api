from pydantic import BaseModel

class Record(BaseModel):
  feeling: str
  emotion: str
  text: str

class RecordUpdate(BaseModel):
  feeling: str | None = None
  emotion: str | None = None
  text: str | None = None