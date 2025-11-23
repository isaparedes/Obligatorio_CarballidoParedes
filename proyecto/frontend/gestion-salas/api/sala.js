// GET /salas
export const getSalas = async () => {
  const accessToken = localStorage.getItem("token");
  const url = "http://localhost:5000/salas/";
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
      console.log("Salas obtenidas:", data);
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
      throw new Error(`Fallo al obtener las salas: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /salas/:nombre_sala/:edificio
export const getSala = async (nombre_sala, edificio) => {
  const accessToken = localStorage.getItem("token");
  const url = `http://localhost:5000/salas/${nombre_sala}/${edificio}`;
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
      console.log("Sala obtenida:", data);
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
      throw new Error(`Fallo al obtener la sala: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// POST /salas
export const createSala = async (newSalaData) => {
  const accessToken = localStorage.getItem("token");
  const url = "http://localhost:5000/salas";

  const body = {
    nombre_sala: newSalaData.nombre_sala,
    edificio: newSalaData.edificio,
    capacidad: newSalaData.capacidad,
    tipo_sala: newSalaData.tipo_sala
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
      const salaCreada = await response.json();
      console.log("Sala creada exitosamente:", salaCreada);
      return salaCreada;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.error);
      throw new Error(`Fallo al crear la sala: ${errorData.error}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// PUT /salas/:nombre_sala/:edificio
export const editSala = async (nombre_sala, edificio, changedSalaData) => {
  const accessToken = localStorage.getItem("token");
  const url = `http://localhost:5000/salas/${nombre_sala}/${edificio}`;

  const body = {
    capacidad: changedSalaData.capacidad,
    tipo_sala: changedSalaData.tipo_sala
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
      const salaEditada = await response.json();
      console.log("Sala editada exitosamente:", salaEditada);
      return salaEditada;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message || "Error desconocido");
      throw new Error(`Fallo al editar la sala: ${errorData.message || "Error desconocido"}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// DELETE /salas/:nombre_sala/:edificio
export const deleteSala = async (nombre_sala, edificio) => {
  const accessToken = localStorage.getItem("token");
  const url = `http://localhost:5000/salas/${nombre_sala}/${edificio}`;

  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      console.log(
        `Sala ${nombre_sala} del ${edificio} eliminada exitosamente (204 No Content).`
      );
      return response.status;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else if (response.status === 404) {
      throw new Error(`Sala ${nombre_sala} de ${edificio} no encontrada.`);
    } else {
      const errorData = await response.json();
      console.error(
        `Error ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al eliminar la sala: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /salas/turnos/disponibles
export const getTurnosDisponiblesSegunSala = async (nombreSala, edificio, fecha) => {
  const accessToken = localStorage.getItem("token");
  const fechaStr = fecha instanceof Date ? fecha.toISOString() : fecha;

  const url = `http://localhost:5000/salas/turnos/disponibles?nombre_sala=${encodeURIComponent(nombreSala)}&edificio=${encodeURIComponent(edificio)}&fecha=${encodeURIComponent(fechaStr)}`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${accessToken}`, 
      },
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Turnos disponibles:", data.turnos_disponibles);
      return data.turnos_disponibles;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      throw new Error(errorData.error || "Error al obtener turnos");
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};
