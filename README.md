# Obligatorio Base de Datos I
## Vanesa Carballido e Isabela Paredes

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
    SECRET_KEY=secret_key # Ver esto!!
    DB_HOST=127.0.0.1
    DB_PORT=3307
    DB_USER=root
    DB_PASSWORD=rootpassword
    DB_NAME=gestion_salas
- Inicializar el proyecto:
    - 1. Ir a ruta: cd backend
    - 2. Correr proyecto: python app.py

### Frontend: 
- Ir a ruta: cd frontend
- Ir a ruta: cd gestion-salas
- Instalar dependencias: npm i
- Correr proyecto: npm run dev

