export interface SolveResponse {
  groups: string[][];
}

export interface GameChallengeResponse {
  challenge_word: string;
  message: string;
}

export interface SubmitAnswerRequest {
  challenge_word: string;
  submitted_word: string;
  user_id: number;
}

export interface SubmitAnswerResponse {
  correct: boolean;
  points_awarded: number;
  total_points: number;
  message: string;
}