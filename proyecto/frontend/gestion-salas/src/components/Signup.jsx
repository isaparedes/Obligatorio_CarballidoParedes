import { useState, useEffect } from 'react';
import delay from 'delay';
import { useNavigate } from "react-router-dom";
import "./App.css"
import { handleSignup } from '../../api/auth';
import { getProgramas } from '../../api/programa';

export default function SignUp() {
  const [ci, setCi] = useState("");
  const [nombre, setNombre] = useState("");
  const [apellido, setApellido] = useState("");
  const [programa, setPrograma] = useState("");
  const [rol, setRol] = useState("");
  const [correo, setCorreo] = useState("");
  const [contrasena, setContrasena] = useState("");
  const [error, setError] = useState("");
  const [registro, setRegistro] = useState("");

  const [programas, setProgramas] = useState([]);

  const navigate = useNavigate()

  useEffect(() => {
    getProgramas()
      .then((programas_academicos) => {
        setProgramas(programas_academicos);
      })
      .catch((err) => {
        console.error("Error al cargar programas académicos:", err);
      });
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setRegistro("");

    if (ci.length < 8) {
      setError("La cédula debe tener al menos 8 números.");
      return;
    }

    let dominio_correcto = "@correo.ucu.edu.uy";
    if (rol === "docente") {
      dominio_correcto = "@ucu.edu.uy"
    }

    if (!correo.includes(dominio_correcto)) {
      setError(`El email no es válido. Debe contener: ${dominio_correcto}`);
      return;
    }

    if (contrasena.length < 8) {
      setError("La contraseña debe contener al menos 8 dígitos");
      return;
    }

    try {
      const usuario = await handleSignup(ci, nombre, apellido, programa, rol, correo, contrasena);
      setRegistro("Usuario registrado correctamente");
      await delay(2000);
      navigate("/login")
    } catch (err) {
      setError(err.message);
    }

  };

  return (
    <div className='inicio'>
      <h1>Ingrese sus datos:</h1>

      {error && <p style={{fontSize: 15}}>{error}</p>}
      {registro && <p style={{fontSize: 15}}>{registro}</p>}
      <form className="datos" onSubmit={handleSubmit}>
        <p className="titulo">Nombre
          <input type="text" value={nombre} placeholder="Ej: Ana" onChange={(e) => setNombre(e.target.value)} required />
        </p>
        <p className="titulo">Apellido
          <input type="text" value={apellido} placeholder="Ej: Rodríguez" onChange={(e) => setApellido(e.target.value)} required />
        </p>
        <p className="titulo">Cédula
          <input type="text" value={ci} placeholder="Ej: 12345678" onChange={(e) => setCi(e.target.value)} required />
        </p>
        <p className="titulo">Correo
          <input type="email" value={correo} placeholder="Ej: ana@correo.ucu.edu.uy" onChange={(e) => setCorreo(e.target.value)} required />
        </p>
        <p className="titulo">Contraseña
          <input type="password" value={contrasena} placeholder="********" onChange={(e) => setContrasena(e.target.value)} required />
        </p>
        <p className="titulo">Programa Académico
          <select value={programa} onChange={(e) => setPrograma(e.target.value)} required>
            <option value="">Seleccione un programa</option>
            {programas && 
              programas.map((p, index) => (
              <option key={index} value={p.nombre_programa}>
                {p.nombre_programa}
              </option>
            ))}
          </select>
        </p>
        <p className="titulo">Rol
          <select value={rol} onChange={(e) => setRol(e.target.value)} required>
            <option value="">Seleccione un rol</option>
            <option value="alumno">Alumno</option>
            <option value="docente">Docente</option>
          </select>
        </p>

        <div className='inicio'>
          <button type="submit">Registrarse</button>
        </div>
      </form>
    </div>
  );
}
