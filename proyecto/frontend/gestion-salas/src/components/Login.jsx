import { useState } from 'react';
import "./App.css";
import delay from 'delay';
import { handleLogin } from '../../api/auth';
import { useAuth } from '../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import { getParticipantePorEmail } from '../../api/participante';

export default function Login() {
  const [correo, setCorreo] = useState("");
  const [contrasena, setContrasena] = useState("");
  const [error, setError] = useState("");
  const [sesion, setSesion] = useState("");

  const { login } = useAuth();

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const data = await handleLogin(correo, contrasena);
      login(data.user, data.token); 
      setSesion("Bienvenido/a");
      const usuario = await getParticipantePorEmail(correo);
      localStorage.setItem("ci", usuario["ci"])
      await delay(2000)
      navigate("/reserva/form")
    } catch (err) {
      setError(err.message);
    }
  };



  return (
    <div className="inicio">
      <h1>Iniciar sesión</h1>

      {error && <p className="error">{error}</p>}
      {sesion && <p>{sesion}</p>}
      <form className="datos" onSubmit={handleSubmit}> 
        <p className="titulo">
          <input
            type="text"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
            placeholder='email'
            required
          />
        </p>

        <p className="titulo">
          <input
            type="password"
            value={contrasena}
            onChange={(e) => setContrasena(e.target.value)}
            placeholder='contraseña'
            required
          />
        </p>

        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
}
