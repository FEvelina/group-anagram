import type {
  SolveResponse,
  GameChallengeResponse,
  SubmitAnswerRequest,
  SubmitAnswerResponse,
} from "./api";

const API_BASE_URL = "http://localhost:8000";

export async function solveAnagrams(words: string[]): Promise<SolveResponse> {
  const response = await fetch(`${API_BASE_URL}/anagrams/solve`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ words }),
  });

  if (!response.ok) {
    throw new Error("Failed to solve anagrams");
  }

  return response.json();
}

export async function getChallenge(): Promise<GameChallengeResponse> {
  const response = await fetch(`${API_BASE_URL}/game/challenge`);

  if (!response.ok) {
    throw new Error("Failed to fetch challenge");
  }

  return response.json();
}

export async function submitAnswer(
  payload: SubmitAnswerRequest,
): Promise<SubmitAnswerResponse> {
  const response = await fetch(`${API_BASE_URL}/game/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Failed to submit answer");
  }

  return response.json();
}
