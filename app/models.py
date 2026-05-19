
from pydantic import BaseModel, Field
from typing import Optional

class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)
    color: Optional[str] = "yellow"

class NoteResponse(NoteCreate):
    id: int
