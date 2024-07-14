from pydantic import BaseModel

class Credenciales(BaseModel):
    usuario: str
    contraseña: str
