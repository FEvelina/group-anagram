from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.game import (
    GameChallengeResponse,
    SubmitAnswerRequest,
    SubmitAnswerResponse,
)
from app.services.game_service import get_random_challenge_word, check_and_score_answer

router = APIRouter(prefix="/game", tags=["game"])


@router.get("/challenge", response_model=GameChallengeResponse)
def get_challenge(db: Session = Depends(get_db)):
    challenge_word = get_random_challenge_word(db)
    if not challenge_word:
        raise HTTPException(status_code=404, detail="No valid challenge found in database.")

    return GameChallengeResponse(
        challenge_word=challenge_word,
        message="Find another valid anagram for this word."
    )


@router.post("/submit", response_model=SubmitAnswerResponse)
async def submit_answer(payload: SubmitAnswerRequest, db: Session = Depends(get_db)):
    correct, points_awarded, total_points, message = await check_and_score_answer(
        db=db,
        challenge_word=payload.challenge_word,
        submitted_word=payload.submitted_word,
        user_id=payload.user_id,
    )

    return SubmitAnswerResponse(
        correct=correct,
        points_awarded=points_awarded,
        total_points=total_points,
        message=message,
    )