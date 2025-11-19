from dao.auth_dao import (
    get_usuario_por_correo,
    crear_usuario
)

from dao.participante_dao import (
    insertar_participante,
    insertar_participante_programa
)

from utils.session import (
    hash_password,
    verify_password,
    generate_jwt
)

def servicio_registrar_sesion(data):
    ci = data.get("ci"),
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    nombre_programa = data.get("nombre_programa")
    rol = data.get("rol")
    correo = data.get("correo")
    contrasena = data.get("contrasena")
    
    if get_usuario_por_correo(correo):
        return None, "El correo ya está registrado", 409

    hashed = hash_password(contrasena)

    usuario = crear_usuario(correo, hashed)
    insertar_participante(ci, nombre, apellido, correo)
    insertar_participante_programa(ci, nombre_programa, rol)
    
    return usuario, None, 201


def servicio_iniciar_sesion(data):
    correo = data.get("correo")
    contrasena = data.get("contrasena")

    usuario = get_usuario_por_correo(correo)
    if not usuario:
        return None, "Usuario no encontrado", 401
    
    if not verify_password(contrasena, usuario["contrasena"]):
        return None, "Contraseña incorrecta", 401
    
    token = generate_jwt(correo)

    return token, None, 200
