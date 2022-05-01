import { Routes, Route } from "react-router-dom";

import HomeTab from "./tabs/Home";
import NewPredictionTab from "./tabs/NewPrediction";
import TitleBar from "./components/format/TitleBar";

function App() {
  return (
    <div>
      <TitleBar />
      <Routes>
        <Route path="/" element={<HomeTab />} />
        <Route path="/new-prediction" element={<NewPredictionTab />} />
      </Routes>
    </div>
  );
}

export default App;