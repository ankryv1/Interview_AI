import React from "react";
import Container from "./Container";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const Navbar = () => {
  const { user, loading } = useAuth();

  return (
    <nav className="border-b bg-[#080B12] shadow-sm">
      <Container className="flex items-center justify-between h-16">
        <Link to="/" className="text-2xl font-bold text-orange-300 underline">
          <span className="text-indigo-100">Interview</span>AI
        </Link>

        {!loading && (
          <div className="flex items-center gap-6">
            {user ? (
              <div className = 'flex items-center gap-6'>
                <Link
                  to="/dashboard"
                  className="text-white hover:text-blue-600"
                >
                  Dashboard
                </Link>
                <Link
                  to="/logout"
                  className="text-gray-600 hover:text-blue-600"
                >
                  Logout
                </Link>
              </div>
            ) : (
              <div className="flex items-center gap-4">
                <Link to="/login" className="text-gray-600 hover:text-blue-600">
                  Login
                </Link>

                <Link
                  to="/signup"
                  className="text-gray-600 hover:text-blue-600"
                >
                  Signup
                </Link>
              </div>
            )}
          </div>
        )}
      </Container>
    </nav>
  );
};

export default Navbar;
