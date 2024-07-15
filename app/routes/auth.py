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
    usuario = usuarios.get(credenciales.usuario)
    if not usuario or usuario["contraseña"] != credenciales.contraseña:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"mensaje": "Autenticación exitosa"}


@router.post("/login")
def login(credenciales: Credenciales = Body(...)):
    return autenticar_usuario(credenciales)
