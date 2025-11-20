import { createContext, useContext, useState, useEffect } from "react";

// 👉 1. Crear el contexto
const AuthContext = createContext();

// 👉 2. Hook para usar el contexto en cualquier componente
export const useAuth = () => useContext(AuthContext);

// 👉 3. Provider que envuelve tu aplicación
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);  
  const [token, setToken] = useState(null);
  const [loading, setLoading] = useState(true);
  
  useEffect(() => {
    const storedToken = localStorage.getItem("token");
    const storedUser = localStorage.getItem("user");

    if (storedToken) {
      setToken(storedToken);
    }

    if (storedUser && storedUser !== "undefined") {
      try {
        setUser(JSON.parse(storedUser));
      } catch (err) {
        console.error("Error al parsear usuario:", err);
        localStorage.removeItem("user"); 
      }
    }

    setLoading(false);
  }, []);


  // 👇 función para guardar login
  const login = (userData, tokenData) => {
    setUser(userData);
    setToken(tokenData);
    if (userData) {
      localStorage.setItem("user", JSON.stringify(userData));
    }
    if (tokenData) {
      localStorage.setItem("token", tokenData);
    }
  };

  // 👇 función para cerrar sesión
  const logout = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem("user");
    localStorage.removeItem("token");
  };

  return (
    <AuthContext.Provider value={{ user, token, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
