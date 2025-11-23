# Obligatorio Base de Datos I
### Vanesa Carballido e Isabela Paredes

## Instructivo para correr la aplicación de forma [`local`](#local) y en contenedor [Docker](#docker)

## Local
  
### ✨ Inicializar backend:
- En la terminal del proyecto ir a la ruta backend:
    
      cd backend
        
- Instalar entorno virtual:
  
      python -m venv venv

- Activar entorno virtual según SO:
  
  - En Windows:

          venv\Scripts\activate
  
  - En Linux/macOS:
    
          source venv/bin/activate

- Instalar dependencias:
  
      pip install -r requirements.txt
        
- Crear archivo **.env** en la carpeta **backend** con los datos de la base de datos:
        
      SECRET_KEY="secret_key"
      
      DB_HOST=127.0.0.1
      
      DB_PORT=3307
      
      DB_USER=root
      
      DB_PASSWORD=rootpassword
      
      DB_NAME=gestion_salas
  
- Correr backend:
    
      python app.py   

   
### ✨ Inicializar frontend:
- Ir a la ruta frontend:

      cd frontend
  
- Ir a la ruta gestion-salas:

      cd gestion-salas
    
- Instalar dependencias:

      npm i

- Correr proyecto (asegurarse de tener el backend y la base de datos corriendo para que funcione correctamente):

      npm run dev


## Docker

### ✨ Ir a proyecto/backend:

    cd backend

### ✨ Crear archivo **.env** con los datos de la base de datos:


      SECRET_KEY="secret_key"
      
      DB_HOST=db
      
      DB_PORT=3306
      
      DB_USER=root
      
      DB_PASSWORD=rootpassword
      
      DB_NAME=gestion_salas

### ✨ Levantar proyecto: 
    cd proyecto
    docker compose build
    docker compose up


