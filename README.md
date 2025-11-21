# Obligatorio Base de Datos I
### Vanesa Carballido e Isabela Paredes

## Instructivo para correr la aplicación de forma local:
  
## ✨ Inicializar backend:
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
        
- Crear archivo **.env** en la carpeta **backend** con este contenido:
        
        SECRET_KEY="secret_key"
      
        DB_HOST=127.0.0.1
      
        DB_PORT=3307
      
        DB_USER=root
      
        DB_PASSWORD=rootpassword
      
        DB_NAME=gestion_salas
  
- Correr backend:
    
      python app.py   

   
## ✨ Inicializar frontend:
- Ir a la ruta frontend:

      cd frontend
  
- Ir a la ruta gestion-salas:

        cd gestion-salas
    
- Instalar dependencias:

      npm i

- Correr proyecto (asegurarse de tener el backend corriendo para que funcione correctamente):

      npm run dev




