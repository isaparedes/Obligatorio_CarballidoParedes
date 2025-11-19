import { Navigate } from "react-router-dom";

export default function ProtectedRoute({ children, rol }) {
  const token = localStorage.getItem("token");
  const usuarioRol = localStorage.getItem("rol");

  if (!token) return <Navigate to="/login" />;

  if (rol && usuarioRol !== rol) return <Navigate to="/" />;

  return children;
}

