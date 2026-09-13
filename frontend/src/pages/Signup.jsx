import React, { useState } from "react";
import axios from "axios";
import { useNavigate, Link } from "react-router-dom";
import api from "../services/api";
import { FaUser, FaEnvelope, FaLock } from "react-icons/fa";
import signupBanner from "../assets/signup-banner.png";
 
const Signup = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
 
  const handleSignup = async (e) => {
    e.preventDefault();
 
    if (!username || !email || !password) {
      setError("All Fields are required");
      return;
    }
 
    if (username.length < 2) {
      setError("Username must be at least 2 characters");
      return;
    }
 
    if (password.length < 4) {
      setError("Password must be at least 4 characters");
      return;
    }
 
    setError("");
    setLoading(true);
 
    try {
      await api.post(
        `/auth/signup`,
        { username, email, password },
        { withCredentials: true }
      );
 
      navigate("/");
    } catch (error) {
      setError(error.response?.data?.detail || "Signup Failed");
    } finally {
      setLoading(false);
    }
  };
 
  return (
    <div className="min-h-screen flex flex-col md:flex-row">
      {/* Left side - image panel (hidden on small screens) */}
      <div className="hidden md:block md:w-1/2 ">
        <img
          src={signupBanner}
          alt="InterviewAI"
          className="w-full h-full object-cover"
        />
      </div>
 
      {/* Right side - signup form */}
      <div className="flex-1 flex items-center justify-center px-6 py-12 bg-gray-200">
        <div className="w-full max-w-sm bg-white rounded-2xl shadow-xl border border-gray-100 p-8">
          {/* Logo shown only on mobile since the image panel is hidden */}
          <h1 className="text-2xl font-bold text-blue-600 mb-6 md:hidden">
            InterviewAI
          </h1>
 
          <h2 className="text-3xl font-bold text-gray-900">Create account</h2>
          <p className="text-gray-600 mt-2 mb-8">
            Sign up to start your interview practice.
          </p>
 
          <form onSubmit={handleSignup} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Username
              </label>
              <div className="relative">
                <FaUser className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder="yourname"
                  className="w-full border border-gray-300 rounded-lg pl-10 pr-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-blue-600"
                />
              </div>
            </div>
 
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Email
              </label>
              <div className="relative">
                <FaEnvelope className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  className="w-full border border-gray-300 rounded-lg pl-10 pr-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-blue-600"
                />
              </div>
            </div>
 
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Password
              </label>
              <div className="relative">
                <FaLock className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full border border-gray-300 rounded-lg pl-10 pr-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-blue-600"
                />
              </div>
            </div>
 
            {error && (
              <p className="text-red-600 text-sm bg-red-50 border border-red-200 rounded-lg px-4 py-2">
                {error}
              </p>
            )}
 
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 disabled:opacity-60 text-white font-semibold py-2.5 rounded-lg shadow-md hover:shadow-lg transition-all"
            >
              {loading ? "Creating account..." : "Sign Up"}
            </button>
          </form>
 
          <p className="text-center text-gray-600 text-sm mt-8">
            Already have an account?{" "}
            <Link to="/login" className="text-blue-600 font-medium hover:underline">
              Log in
            </Link>
          </p>
        </div>
      </div>
    </div>
  );
};
 
export default Signup;