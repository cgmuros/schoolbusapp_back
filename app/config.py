from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene las variables de entorno
SECRET_KEY = os.getenv("SECRET_KEY")
