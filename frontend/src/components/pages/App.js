import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import CustomerList from "./pages/CustomerList";
import Login from "./pages/Login";
import PrivateRoute from "./components/PrivateRoute";

function App() {
  return (
    <Router>
      <nav>
        <Link to="/">Customers</Link> | <Link to="/login">Login</Link>
      </nav>
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRoute>
              <CustomerList />
            </PrivateRoute>
          }
        />
        <Route path="/login" element={<Login />} />
      </Routes>
    </Router>
  );
}

export default App;
