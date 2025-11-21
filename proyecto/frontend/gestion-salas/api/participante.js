// GET /participantes
export const getParticipantes = async () => {
  const accessToken = localStorage.getItem("token");
  const url = "http://localhost:5000/participantes/";
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
      console.log("Participantes obtenidos:", data);
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
      throw new Error(`Fallo al obtener los participantes: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /participantes/:ci
export const getParticipante = async (accessToken, ci) => {
  const url = `http://localhost:5000/participantes/${ci}`;
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
      console.log("Participante obtenido:", data);
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
      throw new Error(`Fallo al obtener el participante: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /participantes?email=usuario@ucu.edu.uy
export const getParticipantePorEmail = async (email) => {
  const accessToken = localStorage.getItem("token");
  const url = `http://localhost:5000/participantes?email=${encodeURIComponent(email)}`;

  const response = await fetch(url, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${accessToken}`,
      Accept: "application/json",
    },
  });

  if (!response.ok) throw new Error("Error al obtener participante");
  return await response.json();
};



// POST /participantes
const createParticipante = async (accessToken, newParticipanteData) => {
  const url = "http://localhost:5000/participantes";

  const body = {
    ci: newParticipanteData.ci,
    nombre: newParticipanteData.nombre,
    apellido: newParticipanteData.apellido,
    email: newParticipanteData.email
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
      const participanteCreado = await response.json();
      console.log("Participante creado exitosamente:", participanteCreado);
      return participanteCreado;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message);
      throw new Error(`Fallo al crear el participante: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// PUT /participantes/:ci
const editParticipante = async (accessToken, ci, changedParticipanteData) => {
  const url = `http://localhost:5000/participantes/${ci}`;

  const body = {
    nombre: changedParticipanteData.nombre,
    apellido: changedParticipanteData.apellido,
    email: changedParticipanteData.email
  };

  try {
    const response = await fetch(url, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`,
      },
      body: JSON.stringify(body),
    });

    if (response.ok) {
      const participanteEditado = await response.json();
      console.log("Participante editado exitosamente:", participanteEditado);
      return participanteEditado;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message || "Error desconocido");
      throw new Error(`Fallo al editar el participante: ${errorData.message || "Error desconocido"}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// DELETE /participantes/:ci
const deleteParticipante = async (accessToken, ci) => {
  const url = `http://localhost:5000/participantes/${ci}`;

  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      console.log(
        `Participante con CI ${ci} eliminado exitosamente (204 No Content).`
      );
      return response.status;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else if (response.status === 404) {
      throw new Error(`Participante con CI ${ci} no encontrado.`);
    } else {
      const errorData = await response.json();
      console.error(
        `Error ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al eliminar el participante: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};
