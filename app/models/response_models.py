from pydantic import BaseModel
from typing import List


class Citation(BaseModel):
    page: int
    snippet: str


class QuestionResponse(BaseModel):
    answer: str
    citations: List[Citation]
