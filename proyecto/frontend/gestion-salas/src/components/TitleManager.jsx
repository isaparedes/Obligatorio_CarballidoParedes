import { useEffect } from "react";
import { useLocation } from "react-router-dom";

export default function TitleManager() {
  const location = useLocation();

  useEffect(() => {
    const titles = {
      "/": "Inicio | Gestión de salas",
      "/login": "Login | Gestión de salas",
      "/signup": "Registro | Gestión de salas",
      "/reserva/form": "Reserva sala | Gestión de salas",
      "/adminABM": "Administración | Gestión de salas",
      "/metricaBI": "Métricas | Gestión de salas"
    };

    document.title = titles[location.pathname] || "Gestión de salas";
  }, [location.pathname]);

  return null;
}
