from fastapi import APIRouter, Body, HTTPException, status
from typing import Dict
from ..models import Credenciales

router = APIRouter()

# Simulamos una base de datos de usuarios
usuarios = {
    "usuario1": {"nombre": "cgmuros@gmail.com", "contraseña": "alfa1414"},
    "usuario2": {"nombre": "ilsesilva@gmail.com", "contraseña": "alfa1414"},
}


def autenticar_usuario(credenciales: Credenciales) -> Dict[str, str]:
    for usuario_data in usuarios.values():
        if usuario_data["nombre"] == credenciales.usuario and usuario_data["contraseña"] == credenciales.contraseña:
            return {"mensaje": "Autenticación exitosa"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )


@router.post("/login")
def login(credenciales: Credenciales = Body(...)):
    return autenticar_usuario(credenciales)
