// GET /sanciones
const getSanciones = async (accessToken) => {
  const url = "http://localhost:5000/sanciones";
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Sanciones obtenidas:", data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las sanciones: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /sanciones/:ci_participante
const getSancionesPorCI = async (accessToken, ci_participante) => {
  const url = `http://localhost:5000/sanciones/${ci_participante}`;
  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        Accept: "application/json",
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log(`Sanciones obtenidas del participante ${ci_participante}:`, data);
      return data;
    } else if (response.status === 401) {
      console.error("Error 401: Token Bearer no válido o ausente.");
      throw new Error("No autorizado. Por favor, vuelve a iniciar sesión.");
    } else {
      const errorData = await response.json();
      console.error(
        `Error HTTP ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al obtener las sanciones del participante ${ci_participante}: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// POST /sanciones
const createSancion = async (accessToken, newSancionData) => {
  const url = "http://localhost:5000/sanciones";

  const body = {
    ci_participante: newSancionData.ci_participante,
    fecha_inicio: newSancionData.fecha_inicio.toISOString()
  };

  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify(body),
    });

    if (response.ok) {
      const sancionCreada = await response.json();
      console.log("Sanción creada exitosamente:", sancionCreada);
      return sancionCreada;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message);
      throw new Error(`Fallo al crear la sanción: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// DELETE /sanciones/:ci_participante/:fecha_inicio/:fecha_fin
const deleteParticipante = async (accessToken, ci_participante, fecha_inicio, fecha_fin) => {
  const url = `http://localhost:5000/sanciones/${ci_participante}/${fecha_inicio}/${fecha_fin}`;

  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      console.log(
        `Sanción de participante ${ci_participante} (${fecha_inicio} - ${fecha_fin}) eliminada exitosamente (204 No Content).`
      );
      return response.status;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else if (response.status === 404) {
      throw new Error(`Sanción con CI ${ci} no encontrado.`);
    } else {
      const errorData = await response.json();
      console.error(
        `Error ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al eliminar la sanción del participante ${ci_participante} (${fecha_inicio} - ${fecha_fin}): ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};
