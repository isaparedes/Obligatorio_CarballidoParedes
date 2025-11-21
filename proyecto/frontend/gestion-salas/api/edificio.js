// GET /edificios
export const getEdificios = async () => {
  const accessToken = localStorage.getItem("token");
  const url = "http://localhost:5000/edificios";
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
      console.log("Edificios obtenidos:", data);
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
      throw new Error(`Fallo al obtener los edificios: ${errorData.message}`);
    }
  } catch (error) {
    console.error("Error de red o del servidor:", error);
    throw error;
  }
};