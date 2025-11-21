from dao.participante_dao import (
    obtener_participantes, 
    obtener_participante, 
    obtener_participante_por_email,
    obtener_rol_programa,
    insertar_participante, 
    insertar_participante_programa,
    actualizar_participante, 
    eliminar_participante
)

# Obtener todos
def service_obtener_participantes():
    return obtener_participantes()

# Obtener por CI
def service_obtener_participante(ci):
    return obtener_participante(ci)

# Obtener por email
def service_obtener_participante_por_email(email):
    return obtener_participante_por_email(email)

# Obtener rol y programa por CI
def service_obtener_rol_programa(ci):
    return obtener_rol_programa(ci)

# Crear participante
def service_crear_participante(data):

    if obtener_participante(data["ci"]):
        return None, "Ya existe un usuario con dicha cédula", 409

    nuevo = insertar_participante(
        data["ci"],
        data["nombre"],
        data["apellido"],
        data["correo"]
    )

    return nuevo, None, 201

# Crear participante con su programa
def service_crear_participante_programa(data):

    if obtener_participante(data["ci"]):
        return None, "Ya existe un usuario con dicha cédula", 409

    nuevo = insertar_participante_programa(
        data["ci"],
        data["nombre_programa"],
        data["rol"]
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

