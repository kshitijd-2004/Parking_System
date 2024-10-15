import Driver from "./components/Driver";
import "./App.css";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <div className="welcome-container">
      <div className="welcome-message">
        <h1>Welcome To Parking Management System</h1>
      </div>

      <div className="buttons">
        <a href="/manage-drivers"></a>
        <button className="manage-drivers">Manage Drivers</button>
        <button className="manage-vehicles">Manage Vehicles</button>
        <button className="manage-citations">Manage Citations</button>
        <button className="manage-permit">Manage Permits</button>
        <button className="manage-parkinglot">Manage Parking Lots</button>
        <button className="manage-zone">Manage Zones</button>
        <button className="manage-spaces">Manage Spaces</button>
        <button className="manage-vehiclecitation">Manage Vehicle Citations</button>
      </div>
    </div>
  );
}

export default App;
