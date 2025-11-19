from dao.auth_dao import (
    get_usuario_por_correo,
    crear_usuario
)
from utils.session import (
    hash_password,
    verify_password,
    generate_jwt
)

def servicio_registrar_sesion(data):
    correo = data.get("correo")
    contrasena = data.get("contrasena")

    if not correo or not contrasena:
        return None, "Correo y contraseña son obligatorios", 400
    
    if get_usuario_por_correo(correo):
        return None, "El correo ya está registrado", 409

    hashed = hash_password(contrasena)

    usuario = crear_usuario(correo, hashed)
    return usuario, None, 201


def servicio_iniciar_sesion(data):
    correo = data.get("correo")
    contrasena = data.get("contrasena")

    if not correo or not contrasena:
        return None, "Falta correo o contraseña", 400

    usuario = get_usuario_por_correo(correo)
    if not usuario:
        return None, "Usuario no encontrado", 401
    
    if not verify_password(contrasena, usuario["contrasena"]):
        return None, "Credenciales inválidas", 401
    
    token = generate_jwt(correo)

    return token, None, 200
