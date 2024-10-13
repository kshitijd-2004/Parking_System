import { useState } from "react";

interface Driver {
  id: number;
  name: string;
  handicap: boolean;
  status: "active" | "inactive";
}

function Driver() {
  const [drivers, setDrivers] = useState<Driver[]>([
    { id: 1, name: "John Doe", handicap: false, status: "active" },
    { id: 2, name: "Jane Smith", handicap: true, status: "inactive" },
  ]);
  return(
    <>
    <h2>Drivers</h2>
    <ul>
        {drivers.map(driver =>  (
            <li key={driver.id}>
                {driver.name}: {driver.handicap ? "Handicapped" : "Non-Handicapped"}, {driver.status}
            </li>
        ))}
    </ul>
    </>
  )
}

export default Driver
