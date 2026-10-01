import React, { useState } from "react";
import Container from "./Container";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import api from "../../services/api";
import toast from "react-hot-toast";

const Navbar = () => {
  const { user, loading, setUser } = useAuth();
  const [isLoggingOut, setIsLoggingOut] = useState(false);
  const navigate = useNavigate();

  const handleLogout = async () => {
    setIsLoggingOut(true);
    try {
      await api.post("/auth/logout");
      if (setUser) setUser(null);
      toast.success("Logged out successfully");
      navigate("/login");
    } catch (err) {
      const message =
        err.response?.data?.detail ||
        err.response?.data?.message ||
        "Logout failed. Please try again.";
      toast.error(message);
    } finally {
      setIsLoggingOut(false);
    }
  };

  return (
    <nav className="border-b border-slate-800 bg-[#080B12]/80 backdrop-blur-md sticky top-0 z-50">
      <Container className="flex items-center justify-between h-16">
        {/* Brand Logo */}
        <Link to="/" className="text-2xl font-extrabold tracking-tight">
          <span className="text-white">Interview</span>
          <span className="bg-gradient-to-r from-orange-400 to-amber-200 bg-clip-text text-transparent">
            AI
          </span>
        </Link>

        {!loading && (
          <div className="flex items-center gap-6">
            {user ? (
              <div className="flex items-center gap-4">
                <Link
                  to="/dashboard"
                  className="text-sm font-medium text-slate-300 hover:text-white transition-colors"
                >
                  Dashboard
                </Link>

                <button
                  onClick={handleLogout}
                  disabled={isLoggingOut}
                  className="px-4 py-1.5 text-sm font-medium text-red-400 bg-red-500/10 border border-red-500/20 rounded-lg hover:bg-red-500/20 hover:border-red-500/40 transition-all disabled:opacity-50"
                >
                  {isLoggingOut ? "Logging out..." : "Logout"}
                </button>
              </div>
            ) : (
              <div className="flex items-center gap-3">
                <Link
                  to="/login"
                  className="px-4 py-1.5 text-sm font-medium text-slate-300 hover:text-white transition-colors"
                >
                  Login
                </Link>

                <Link
                  to="/signup"
                  className="px-4 py-1.5 text-sm font-semibold text-white bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-600 hover:to-amber-600 rounded-lg shadow-md shadow-orange-500/20 transition-all"
                >
                  Sign Up
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