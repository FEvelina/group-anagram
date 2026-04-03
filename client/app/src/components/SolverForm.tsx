import { useState, type SubmitEvent } from "react";
import { solveAnagrams } from "../client";

export default function SolverForm() {
  const [input, setInput] = useState<string>("");
  const [groups, setGroups] = useState<string[][]>([]);
  const [error, setError] = useState<string>("");

  const handleSubmit = async (e: SubmitEvent) => {
    e.preventDefault();
    setError("");

    /* eslint-disable @typescript-eslint/no-explicit-any */
    try {
      const words = input
        .split(",")
        .map((w) => w.trim())
        .filter(Boolean);

      const data = await solveAnagrams(words);
      setGroups(data.groups);
    } catch (err: any) {
      setError(err.message || "Something went wrong");
    }
  };

  return (
    <div>
      <h2>Anagram Solver</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="eat, tea, tan, ate, nat, bat"
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">Solve</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <div>
        {groups.map((group, index) => (
          <div key={index}>[{group.join(", ")}]</div>
        ))}
      </div>
    </div>
  );
}
