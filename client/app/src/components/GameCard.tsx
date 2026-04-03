import { useEffect, useState, useCallback, type SubmitEvent } from "react";
import { getChallenge, submitAnswer } from "../client";
import type { GameChallengeResponse, SubmitAnswerResponse } from "../api";

export default function GameCard() {
  const [challenge, setChallenge] = useState<GameChallengeResponse | null>(
    null,
  );
  const [answer, setAnswer] = useState<string>("");
  const [result, setResult] = useState<SubmitAnswerResponse | null>(null);
  const [error, setError] = useState<string>("");

  //also need to add auth, for testing purpose, keep user static
  const userId = 1;

  const fetchChallenge = useCallback(async () => {
    try {
      const data = await getChallenge();
      setChallenge(data);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Failed to load challenge");
      }
    }
  }, []);

  useEffect(() => {
    // we leave it be for now, no time to fix everything
    // eslint-disable-next-line react-hooks/set-state-in-effect
    void fetchChallenge();
  }, [fetchChallenge]);

  async function handleNewChallenge() {
    setAnswer("");
    setResult(null);
    setError("");
    await fetchChallenge();
  }

  async function handleSubmit(e: SubmitEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!challenge) return;

    try {
      setError("");

      const data = await submitAnswer({
        challenge_word: challenge.challenge_word,
        submitted_word: answer,
        user_id: userId,
      });

      setResult(data);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("Failed to submit answer");
      }
    }
  }

  return (
    <div>
      <h2>Anagram Game</h2>

      {challenge && (
        <>
          <p>
            Word: <strong>{challenge.challenge_word}</strong>
          </p>

          <form onSubmit={handleSubmit}>
            <input
              type="text"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder="Type another anagram"
            />
            <button type="submit">Submit</button>
          </form>
        </>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div>
          <p>{result.message}</p>
          <p>Total points: {result.total_points}</p>
        </div>
      )}

      <button onClick={handleNewChallenge}>New Challenge</button>
    </div>
  );
}
