import Home from "./components/Home";
import Driver from "./components/Driver";
import Citation from "./components/Citation";
import ParkingLot from "./components/ParkingLot";
import Permit from "./components/Permit";
import Space from "./components/Space";
import Vehicle from "./components/Vehicle";
import Zone from "./components/Zone";
import VehicleCitation from "./components/VehicleCitation";

import "./App.css";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Home />} />
        <Route path="/manage-drivers" element={<Driver />} />
        <Route path="/manage-citations" element={<Citation />} />
        <Route path="/manage-vehicles" element={<Vehicle />} />
        <Route path="/manage-permits" element={<Permit />} />
        <Route path="/manage-parkinglots" element={<ParkingLot />} />
        <Route path="/manage-zones" element={<Zone />} />
        <Route path="/manage-spaces" element={<Space />} />
        <Route path="/manage-vehiclecitation" element={<VehicleCitation />} />
      </Routes>
    </Router>
  );
}

export default App;
