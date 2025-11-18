from dao.participante_dao import (
    obtener_participantes, 
    obtener_participante, 
    insertar_participante, 
    actualizar_participante, 
    eliminar_participante
)


# Obtener todos
def service_obtener_participantes():
    return obtener_participantes()

# Obtener por cédula
def service_obtener_participante(ci):
    return obtener_participante(ci)


# Crear participante
def service_crear_participante(data):

    if ( "ci" not in data or "nombre" not in data or "apellido" not in data or "email" not in data):
        return None, "Faltan campos obligatorios", 400

    if obtener_participante(data["ci"]):
        return None, "El participante ya existe", 409

    nuevo = insertar_participante(
        data["ci"],
        data["nombre"],
        data["apellido"],
        data["email"]
    )

    return nuevo, None, 201

# Actualizar participante
def service_actualizar_participante(ci, data):

    if not obtener_participante(ci):
        return None, "Participante no encontrado", 404

    actualizado = actualizar_participante(ci, data)
    return actualizado, None, 200


# Eliminar participante 
def service_eliminar_participante(ci):

    if not obtener_participante(ci):
        return None, "Participante no encontrado", 404

    borrado = eliminar_participante(ci)
    return borrado, None, 200