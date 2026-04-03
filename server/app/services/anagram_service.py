from collections import defaultdict
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.anagram_entry import AnagramEntry


def normalize_word(word: str) -> str:
    return word.strip().lower()


def build_sorted_key(word: str) -> str:
    return "".join(sorted(normalize_word(word)))


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)

    for word in words:
        normalized = normalize_word(word)
        if not normalized:
            continue
        key = build_sorted_key(normalized)
        groups[key].append(normalized)

    return list(groups.values())


def store_words(db: Session, words: list[str]) -> tuple[int, int]:
    inserted = 0
    skipped = 0

    existing_words = set(
        db.scalars(select(AnagramEntry.word).where(AnagramEntry.word.in_([normalize_word(w) for w in words])))
        .all()
    )

    for word in words:
        normalized = normalize_word(word)
        if not normalized:
            skipped += 1
            continue

        if normalized in existing_words:
            skipped += 1
            continue

        entry = AnagramEntry(
            word=normalized,
            sorted_key=build_sorted_key(normalized)
        )
        db.add(entry)
        inserted += 1

    db.commit()
    return inserted, skipped