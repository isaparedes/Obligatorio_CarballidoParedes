import { useNavigate } from 'react-router-dom';
import "./App.css"


export default function Home() {

  const navigate = useNavigate();

  return (
    <div className="inicio">
      <h1>Bienvenido al sistema de gestión de salas</h1>
      <button onClick={() => navigate("/login")} className="small-button">Iniciar sesión</button>
      <button onClick={() => navigate("/signup")} className="small-button">Registrarse</button>
    </div>
  );
}