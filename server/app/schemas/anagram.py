from pydantic import BaseModel, Field
from typing import List


class SolveRequest(BaseModel):
    words: List[str] = Field(..., min_length=1)


class SolveResponse(BaseModel):
    groups: List[List[str]]


class AddWordsResponse(BaseModel):
    inserted_count: int
    skipped_count: int