// GET /reservas
const getSalasMasReservadas = async (accessToken) => {
  const url = "http://localhost:5000/reservas";
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
      console.log("Reservas obtenidas:", data);
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
      throw new Error(`Fallo al obtener las reservas: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// GET /reservas/:id
const getReserva = async (accessToken, id) => {
  const url = `http://localhost:5000/reservas/${id}`;
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
      console.log("Reserva obtenida:", data);
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
      throw new Error(`Fallo al obtener la reserva: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// POST /reservas
const createReserva = async (accessToken, newReservaData) => {
  const url = "http://localhost:5000/reservas";

  const body = {
    nombre_sala: newReservaData.nombre_sala,
    edificio: newReservaData.edificio,
    fecha: newReservaData.fecha.toISOString(),
    turno: newReservaData.turno,
    participantes: newReservaData.participantes
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
      const reservaCreada = await response.json();
      console.log("Reserva creada exitosamente:", reservaCreada);
      return reservaCreada;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message);
      throw new Error(`Fallo al crear la reserva: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// PUT /reservas/:id
const editReserva = async (accessToken, id, changedReservaData) => {
  const url = `http://localhost:5000/reservas/${id}`;

  const body = {
    fecha: changedReservaData.fecha,
    id_turno: changedReservaData.id_turno,
    estado: changedReservaData.estado
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
      const reservaEditada = await response.json();
      console.log("Reserva editada exitosamente:", reservaEditada);
      return reservaEditada;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message || "Error desconocido");
      throw new Error(`Fallo al editar la reserva: ${errorData.message || "Error desconocido"}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};

// DELETE /reservas/:id
const deleteReserva = async (accessToken, id) => {
  const url = `http://localhost:5000/reservas/${id}`;

  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    });

    if (response.status === 204) {
      console.log(
        `Reserva con ID ${id} eliminada exitosamente (204 No Content).`
      );
      return response.status;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else if (response.status === 404) {
      throw new Error(`Reserva con ID ${id} no encontrada.`);
    } else {
      const errorData = await response.json();
      console.error(
        `Error ${response.status}:`,
        errorData.message || "Error desconocido"
      );
      throw new Error(`Fallo al eliminar la reserva: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
}; 

// POST /reservas/salas/disponibles
const getSalasDisponibles = async (accessToken, requestedReservaData) => {
  const url = "http://localhost:5000/reservas/salas/disponibles";

  const body = {
    fecha: requestedReservaData.fecha.toISOString(),
    ci_reservante: requestedReservaData.ci_reservante,
    lista_participantes: requestedReservaData.lista_participantes
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
      const salasDisponibles = await response.json();
      console.log("Salas disponibles obtenidas:", salasDisponibles);
      return salasDisponibles;
    } else if (response.status === 401) {
      throw new Error("No autorizado. Por favor, revisa tu token.");
    } else {
      const errorData = await response.json();
      console.error(`Error ${response.status}:`, errorData.message);
      throw new Error(`Error al obtener salas disponibles: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};


