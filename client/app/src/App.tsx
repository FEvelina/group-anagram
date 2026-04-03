import SolverForm from "./components/SolverForm";
import GameCard from "./components/GameCard";

function App() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Anagram App</h1>

      <SolverForm />
      <hr />
      <GameCard />
    </div>
  );
}

export default App;
