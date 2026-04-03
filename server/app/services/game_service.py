import random
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from app.models.anagram_entry import AnagramEntry
from app.models.user import User
from app.services.anagram_service import normalize_word, build_sorted_key
from app.services.dictionary_service import word_exists_in_dictionary


POINTS_FOR_CORRECT_ANSWER = 10


def get_random_challenge_word(db: Session) -> str | None:
    """
    Pick a word whose sorted_key appears more than once.
    """
    #selecting a word whose sorted_key has more than one apparition
    keys_with_multiple_words = db.execute(
        select(AnagramEntry.sorted_key)
        .group_by(AnagramEntry.sorted_key)
        .having(func.count(AnagramEntry.id) >= 2)
    ).scalars().all()

    if not keys_with_multiple_words:
        return None

    random_key = random.choice(keys_with_multiple_words)

    words = db.execute(
        select(AnagramEntry.word).where(AnagramEntry.sorted_key == random_key)
    ).scalars().all()

    if not words:
        return None

    return random.choice(words)


async def check_and_score_answer(
    db: Session,
    challenge_word: str,
    submitted_word: str,
    user_id: int,
) -> tuple[bool, int, int, str]:
    challenge_word = normalize_word(challenge_word)
    submitted_word = normalize_word(submitted_word)

    if challenge_word == submitted_word:
        user = db.get(User, user_id)
        total_points = user.points if user else 0
        return False, 0, total_points, "Submitted word must be different from the challenge word."

    challenge_key = build_sorted_key(challenge_word)
    submitted_key = build_sorted_key(submitted_word)

    if challenge_key != submitted_key:
        user = db.get(User, user_id)
        total_points = user.points if user else 0
        return False, 0, total_points, "That word is not an anagram of the challenge word."

    existing_word = db.execute(
        select(AnagramEntry).where(AnagramEntry.word == submitted_word)
    ).scalar_one_or_none()

    if existing_word is None:
        exists_in_dictionary = await word_exists_in_dictionary(submitted_word)
        if not exists_in_dictionary:
            user = db.get(User, user_id)
            total_points = user.points if user else 0
            return False, 0, total_points, "Word not found in dictionary."

        new_entry = AnagramEntry(word=submitted_word, sorted_key=submitted_key)
        db.add(new_entry)

    user = db.get(User, user_id)
    if user is None:
        return False, 0, 0, "User not found."

    user.points += POINTS_FOR_CORRECT_ANSWER
    db.commit()
    db.refresh(user)

    return True, POINTS_FOR_CORRECT_ANSWER, user.points, "Correct answer!"