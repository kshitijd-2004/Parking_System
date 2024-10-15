import Driver from "./components/Driver";
import Home from "./components/Home"
import "./App.css";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />
        <Route path="/manage-drivers" element={<Driver />} />
      </Routes>
    </Router>
  );
}

export default App;
