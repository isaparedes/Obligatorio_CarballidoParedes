import { useEffect, useState } from "react";

export default function Admin() {
  const [salas, setSalas] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/salas")
      .then((res) => res.json())
        .then((data) => setSalas(data));
    }, []);

  return (
    <div className="inicio">
      <h1>Administrador de salas:</h1>

      <h2>Salas registradas</h2>
      <ul>
        {salas.map((s, i) => (
          <li key={i}>
            {s.nombre_sala} - cap {s.capacidad} - {s.edificio}
          </li>
        ))}
      </ul>

      <button>Agregar sala</button>
      <button>Editar sala</button>
      <button>Eliminar sala</button>
    </div>
  );
}
