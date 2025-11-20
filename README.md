# Obligatorio_CarballidoParedes
# Obligatorio Base de Datos I

## Instructivo:

### Proyecto:
- docker-compose up?? Ver esto

- Ir a ruta: cd proyecto

### Backend: 
- Ir a ruta: cd backend 
- Instalar entorno virtual: python -m venv venv
- Activar entorno virtual: 
    - venv\Scripts\activate (Windows)
    - source venv/bin/activate (Linux/macOS)
- Instalar dependencias: pip install -r requirements.txt
- Crear archivo .env en la carpeta backend con este contenido:
    SECRET_KEY=key
    DB_HOST=localhost
    DB_USER=user
    DB_PASSWORD=password
    DB_NAME=db
- Inicializar el proyecto:
    - 1. Ir a ruta: cd backend
    - 2. Correr proyecto: python app.py

### Frontend: 
- Ir a ruta: cd frontend
- Ir a ruta: cd gestion_salas
- Instalar dependencias: npm i
- Correr proyecto: npm run dev

cd backend

python app.py 
