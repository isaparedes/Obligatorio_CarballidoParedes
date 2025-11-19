import { useState } from 'react';
//import { useNavigate } from 'react-router-dom';
import "../App.css";

export default function Login() {
  const [usuario, setUsuario] = useState("");
  const [password, setPassword] = useState("");
  // const navigate = useNavigate();

  //const handleLogin = async (e) => {
    //e.preventDefault();

    //const body = { usuario, password };

    //try {
      //const res = await fetch("http://localhost:5000/login", {
       // method: "POST",
        //headers: { "Content-Type": "application/json" },
       // body: JSON.stringify(body),
     // });

    //} catch (err) {
      //alert("Error de conexión");
   // }
 // };

 //*onSubmit={handleLogin} falta agregarle al input de usuario
  return (
    <div className="inicio">
      <h1>Iniciar sesión</h1>
      <form className="datos"> 
        
        <p className="titulo">
          Usuario
          <input
            type="text"
            value={usuario}
            onChange={(e) => setUsuario(e.target.value)}
            required
          />
        </p>

        <p className="titulo">
          Contraseña
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </p>

        <button type="submit">Ingresar</button>
      </form>
    </div>
  );
}
