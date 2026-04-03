import httpx


async def word_exists_in_dictionary(word: str) -> bool:
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get(url)

    return response.status_code == 200