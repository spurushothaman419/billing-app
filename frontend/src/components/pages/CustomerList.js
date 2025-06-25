import React, { useEffect, useState } from "react";
import api from "../api";

const CustomerList = () => {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    api.get("/customers/")
      .then((res) => setCustomers(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h1>Customers</h1>
      <ul>
        {customers.map((c) => (
          <li key={c.id}>
            {c.name} - {c.email} - {c.phone}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerList;
