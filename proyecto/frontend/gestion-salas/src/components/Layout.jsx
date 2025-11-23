import { Outlet, Link, useNavigate, useLocation } from "react-router-dom";
import BarraBienvenida from "./BarraBienvenida";
import "./Layout.css";
import { useEffect, useState } from "react";
import { getRolPrograma } from "../../api/participante";

export default function Layout() {
  const navigate = useNavigate();
  const location = useLocation();
  const token = localStorage.getItem("token");
  const ci = localStorage.getItem("ci");
  const [rol, setRol] = useState(null);
  const [loadingRol, setLoadingRol] = useState(true);

  useEffect(() => {
    const fetchRol = async () => {
      if (ci) {
        try {
          const data = await getRolPrograma(ci);
          setRol(data.rol);
        } catch (err) {
          console.error("Error obteniendo rol:", err);
          setRol(null);
        }
      } else {
        setRol(null); 
      }
      setLoadingRol(false);
    };
    fetchRol();
  }, [ci]);

  const handleLogout = () => {
    localStorage.clear();
    setRol(null);
    navigate("/login");
  };

  return (
    <div className="layout">
      <header className="barraBienvenida">
        <BarraBienvenida />
        {location.pathname !== "/" && !loadingRol && (
          <nav className="navbar">
            {!token && (
              <>
                <Link className="nav-link" to="/login">Iniciar sesión</Link>
                <Link className="nav-link" to="/signup">Registrarse</Link>
              </>
            )}

            {token && rol === "admin" && (
              <>
                <Link className="nav-link" to="/reserva/form">Reservar</Link>
                <Link className="nav-link" to="/metrica">Métrica</Link>
                <Link className="nav-link" to="/admin">Administración</Link>
                <button className="nav-button" onClick={handleLogout}>Cerrar sesión</button>
              </>
            )}

            {token && rol && rol !== "admin" && (
              <>
                <Link className="nav-link" to="/reserva/form">Reservar</Link>
                <button className="nav-button" onClick={handleLogout}>Cerrar sesión</button>
              </>
            )}
          </nav>
        )}
      </header>

      <main className="contenido">
        <Outlet />
      </main>
    </div>
  );
}
