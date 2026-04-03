from pydantic import BaseModel


class GameChallengeResponse(BaseModel):
    challenge_word: str
    message: str


class SubmitAnswerRequest(BaseModel):
    challenge_word: str
    submitted_word: str
    user_id: int


class SubmitAnswerResponse(BaseModel):
    correct: bool
    points_awarded: int
    total_points: int
    message: str