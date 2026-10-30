from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class student(BaseModel):
    id: Optional[int] = None
    name: str
    course: str
    marks: float = Field(ge=0, le=100)