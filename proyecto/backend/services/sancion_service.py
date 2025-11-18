from dao.sancion_dao import (
    obtener_sanciones, 
    obtener_sanciones_participante, 
    insertar_sancion, 
    actualizar_sancion, 
    eliminar_sancion
)

# Obtener todas
def service_obtener_sanciones():
    return obtener_sanciones()

# Obtener sanciones por CI
def service_obtener_sanciones_participante(ci):
    return obtener_sanciones_participante(ci)


# Crear sanción
def service_crear_sancion(data):

    if ("ci" not in data or 
        "fecha_inicio" not in data or 
        "fecha_fin" not in data):
        return None, "Faltan campos obligatorios", 400

    nueva = insertar_sancion(
        data["ci"],
        data["fecha_inicio"],
        data["fecha_fin"]
    )

    return nueva, None, 201


# Actualizar sanción
def service_actualizar_sancion(id_sancion, data):

    existente = actualizar_sancion(id_sancion, data)
    if not existente:
        return None, "Sanción no encontrada", 404

    return existente, None, 200


# Eliminar sanción 
def service_eliminar_sancion(id_sancion):

    borrado = eliminar_sancion(id_sancion)
    if not borrado:
        return None, "Sanción no encontrada", 404

    return borrado, None, 200
