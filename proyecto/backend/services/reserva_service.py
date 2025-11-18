from dao.reserva_dao import (
    obtener_reservas,
    obtener_reserva,
    insertar_reserva,
    actualizar_reserva,
    eliminar_reserva,
    insertar_reserva_participante,
    eliminar_reserva_participantes
)

from dao.participante_dao import obtener_participante

# Obtener todas
def service_obtener_reservas():
    return obtener_reservas()

# Obtener por id_reserva
def service_obtener_reserva(id_reserva):
    return obtener_reserva(id_reserva)

# Crear reserva
def service_crear_reserva(data):

    nueva = insertar_reserva(
        data["nombre_sala"],
        data["edificio"],
        data["fecha"],
        data["id_turno"],
        data["estado"]
    )

    for ci in data.get("participantes", []):
        if obtener_participante(ci):
            insertar_reserva_participante(nueva["id_reserva"], ci)

    return nueva, None, 201


# Actualizar reserva
def service_actualizar_reserva(id_reserva, data):

    if not obtener_reserva(id_reserva):
        return None, "Reserva no encontrada", 404

    actualizado = actualizar_reserva(id_reserva, data)
    return actualizado, None, 200


# Eliminar reserva
def service_eliminar_reserva(id_reserva):

    if not obtener_reserva(id_reserva):
        return None, "Reserva no encontrada", 404

    eliminar_reserva_participantes(id_reserva)
    eliminar_reserva(id_reserva)

    return {"deleted": id_reserva}, None, 200
