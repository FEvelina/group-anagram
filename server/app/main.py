from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import anagrams, game
from app.database.session import Base, engine

from app.models.anagram_entry import AnagramEntry
from app.models.user import User

app = FastAPI(title="Anagram Game API")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(anagrams.router)
app.include_router(game.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
