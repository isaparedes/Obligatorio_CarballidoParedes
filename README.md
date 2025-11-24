# Obligatorio Base de Datos I
### Vanesa Carballido e Isabela Paredes

## Instructivo para correr la aplicación de forma [`local`](#local) y en contenedor [`Docker`](#docker)

## Local

### Inicializar backend:

- Ir a la ruta proyecto:

      cd proyecto
  
- Ir a la ruta backend:

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

- Crear base de datos local con script **init.sql** de la carpeta **db** 
        
- Crear archivo **.env** en la carpeta **backend** con los datos de tu base de datos:
        
      SECRET_KEY="secret_key"
      DB_HOST=127.0.0.1
      DB_PORT=3307
      DB_USER=root
      DB_PASSWORD=rootpassword
      DB_NAME=gestion_salas
  
- Correr backend:
    
      python app.py   
   
###  Inicializar frontend:

- Ir a la ruta proyecto en otra terminal:

      cd proyecto

- Ir a la ruta frontend:

      cd frontend
  
- Ir a la ruta gestion-salas:

      cd gestion-salas
    
- Instalar dependencias:

      npm i

- Correr proyecto (asegurarse de tener el backend y la base de datos corriendo para que funcione correctamente):

      npm run dev

- Para acceder al frontend utiliza http://localhost:5173 como indicará la terminal
  
## Docker

- Ir a la ruta proyecto:

      cd proyecto
  
- Crear archivo **.env** con los datos de la base de datos en carpeta backend:

      SECRET_KEY="secret_key"
      DB_HOST=db
      DB_PORT=3306
      DB_USER=root
      DB_PASSWORD=rootpassword
      DB_NAME=gestion_salas

- Crear el contenedor en la carpeta proyecto:

      docker compose build

- Correr el contenedor (automáticamente se crea la base de datos, se instalan las dependencias necesarias y se corre el proyecto):

       docker compose up

- El frontend está expuesto en el host a través del puerto 8080, por lo que puede accederse desde fuera del contenedor usando: http://localhost:8080
- La base de datos está mapeada al puerto 3308 en el host, así que para conectarse desde fuera del contenedor se debe usar el puerto 3308.
