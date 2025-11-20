import { useEffect, useState } from "react";
import "./App.css"

export default function Metrica() {
  const [metricas, setMetricas] = useState(null);

  useEffect(() => {
    fetch("http://localhost:5000/metricas")
      .then((res) => res.json())
      .then((data) => setMetricas(data));
  }, []);

  return (
    <div className="inicio">
      <h1>Métricas del Sistema</h1>

      {!metricas && <p>Cargando métricas...</p>}

      {metricas && (
        <div>
          <p>Total de reservas: {metricas.total_reservas}</p>
          <p>Salas más usadas: {metricas.top_sala}</p>
          <p>Promedio participantes: {metricas.promedio_participantes}</p>
        </div>
      )}
    </div>
  );
}