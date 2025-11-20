// POST /signup
export const handleSignup = async (ci, name, last_name, program_name, role, email, password) => {
  const url = "http://localhost:5000/auth/signup";

  const body = {
    ci: ci,
    nombre: name,
    apellido: last_name,
    nombre_programa: program_name,
    rol: role,
    correo: email,
    contrasena: password
  };

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (response.ok) {
      const usuarioCreado = await response.json();
      console.log("Usuario registrado exitosamente:", usuarioCreado);
      return usuarioCreado;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.error);
      throw new Error(`${errorData.error}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// POST /login
export const handleLogin = async (email, password) => {
  const url = "http://localhost:5000/auth/login";

  const body = {
    correo: email,
    contrasena: password,
  };

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Login exitoso. Token recibido:", data.token);
      return data;
    } else {
      const errorData = await response.json();
      console.error(
        "Error de login:",
        errorData.message || "Credenciales inválidas"
      );
      throw new Error(errorData.message || "Fallo de autenticación");
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};