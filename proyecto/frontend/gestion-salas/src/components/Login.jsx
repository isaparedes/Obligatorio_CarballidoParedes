import { useState } from 'react';
import "./App.css"
import { handleLogin } from '../../api/auth';
import { useAuth } from '../contexts/AuthContext';

export default function Login() {
  const [correo, setCorreo] = useState("");
  const [contrasena, setContrasena] = useState("");
  const [error, setError] = useState("");

  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const data = await handleLogin(correo, contrasena);
      login(data.user, data.token); 
      alert("Bienvenido " + data.user);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="inicio">
      <h1>Iniciar sesión</h1>

      {error && <p className="error">{error}</p>}
      <form className="datos" onSubmit={handleSubmit}> 
        <p className="titulo">
          Email
          <input
            type="text"
            value={correo}
            onChange={(e) => setCorreo(e.target.value)}
            required
          />
        </p>

        <p className="titulo">
          Contraseña
          <input
            type="password"
            value={contrasena}
            onChange={(e) => setContrasena(e.target.value)}
            required
          />
        </p>

        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
}
