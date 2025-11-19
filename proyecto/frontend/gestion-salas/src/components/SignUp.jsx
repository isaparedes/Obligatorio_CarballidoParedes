import { useState } from 'react';
import "../App.css";

export default function SignUp() {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");
  const [cedula, setCedula] = useState("");
  const [mail, setMail] = useState("");

  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (cedula.length !== 8 || isNaN(cedula)) {
      setError("La cédula debe tener 8 números.");
      return;
    }

    if (!mail.includes("@")) {
      setError("El email no es válido.");
      return;
    }

    const body = { usuario, password, cedula, mail };

    try {
      const res = await fetch("http://localhost:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
      });

      const data = await res.json();
      alert("Registro completado: " + data.message);

    } catch (err) {
      setError("Error al registrarse.");
      console.error(err);
    }
  };

  return (
    <div className='inicio'>
      <h1>Ingrese sus datos:</h1>

      {error && <p className="error">{error}</p>}

      <form className="datos" onSubmit={handleSubmit}>
        
        <p className="titulo">Usuario
          <input 
            type="text" 
            value={usuario}
            onChange={(e) => setUsuario(e.target.value)}
            required
          />
        </p>

        <p className="titulo"> Contraseña                    
          <input 
            type="password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </p>

        <p className="titulo"> Cédula
          <input 
            type="text" 
            value={cedula}
            onChange={(e) => setCedula(e.target.value)}
            required
          />
        </p>

        <p className="titulo"> Email
          <input 
            type="email" 
            value={mail}
            onChange={(e) => setMail(e.target.value)}
            required
          />
        </p>

        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
}
