from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.anagram import SolveRequest, SolveResponse
from app.services.anagram_service import group_anagrams, store_words

router = APIRouter(prefix="/anagrams", tags=["anagrams"])


@router.post("/solve", response_model=SolveResponse)
def solve_anagrams(payload: SolveRequest, db: Session = Depends(get_db)):
    groups = group_anagrams(payload.words)
    store_words(db, payload.words)
    return SolveResponse(groups=groups)