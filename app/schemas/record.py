from pydantic import BaseModel

class Record(BaseModel):
  emotion_id: int
  title: str | None = None
  text: str
  

class RecordUpdate(BaseModel):
  feeling: str | None = None
  emotion: str | None = None
  text: str | None = None