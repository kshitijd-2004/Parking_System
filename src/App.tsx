import Driver from "./components/Driver";
import "./App.css";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <div className="welcome-container">
      <div className="welcome-message">
        <h1>Welcome To Parking Management System</h1>
      </div>

      <div className='buttons'>
        <a href="/manage-drivers"></a>
        <button className="manage-drivers">Manage Drivers</button>
      </div>
    </div>
  );
}

export default App;
