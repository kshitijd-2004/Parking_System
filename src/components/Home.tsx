import { Link } from "react-router-dom";
import "../App.css";

function Home() {
  return (
    <div className="welcome-container">
      <div className="welcome-message">
        <h1>Welcome To Parking Management System</h1>
      </div>

      <div className="buttons">
        <Link to="/manage-drivers">
          <button className="manage-drivers">Manage Drivers</button>
        </Link>
        <Link to="/manage-vehicles">
          <button className="manage-vehicles">Manage Vehicles</button>
        </Link>
        <Link to="/manage-citations">
          <button className="manage-citations">Manage Citations</button>
        </Link>
        <Link to="/manage-permit">
          <button className="manage-permit">Manage Permits</button>
        </Link>
        <Link to="/manage-parkinglot">
          <button className="manage-parkinglot">Manage Parking Lots</button>
        </Link>
        <Link to="/manage-zone">
          <button className="manage-zone">Manage Zones</button>
        </Link>
        <Link to="/manage-spaces">
          <button className="manage-spaces">Manage Spaces</button>
        </Link>
        <Link to="/manage-vehiclecitation">
          <button className="manage-vehiclecitation">
            Manage Vehicle Citations
          </button>
        </Link>
      </div>
    </div>
  );
}

export default Home;