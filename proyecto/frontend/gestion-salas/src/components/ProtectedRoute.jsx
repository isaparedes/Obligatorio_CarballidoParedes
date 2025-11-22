import { useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { getRolPrograma } from "../../api/participante";

export default function ProtectedRoute({ children, rol }) {
  const token = localStorage.getItem("token");
  const ci = localStorage.getItem("ci");
  const [usuarioRol, setUsuarioRol] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!ci) {
      setLoading(false);
      return;
    }

    const fetchRol = async () => {
      try {
        const rolObtenido = await getRolPrograma(ci);
        console.log(rolObtenido);
        setUsuarioRol(rolObtenido["rol"]);
      } catch (error) {
        console.error("Error obteniendo rol:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchRol();
  }, [ci]);

  if (!token) return <Navigate to="/login" />; // 👈 antes mandabas a reserva

  if (loading) return <div>Cargando...</div>; 

  if (rol && usuarioRol !== rol) return <Navigate to="/" />;

  return children;
}
