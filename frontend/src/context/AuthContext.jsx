import { createContext, useContext, useEffect, useState } from "react";
import api from "../services/api";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true); // to wait, i am checking the backend


  const checkAuth = async () => {
    try {
      const response = await api.get("/auth/me", { withCredentials: true });
        console.log("check auth is running", response);
      setUser(response.data.user);
    } catch (error) {
      setUser(null);
    } finally {
      setLoading(false);
    }
  };


  useEffect(() => {
    checkAuth();
  }, []);

  return (
    <AuthContext.Provider value={{ user, setUser, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};


// Browser refresh
//      ↓
// AuthProvider mounts
//      ↓
// GET /auth/me
//      ↓
// Backend sees cookie
//      ↓
// "Yes, this is user"
//      ↓
// setUser(user)