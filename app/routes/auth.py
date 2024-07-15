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
    return {
        "error": "Credenciales inválidas",
        "code": 401,
        "message": "Las credenciales proporcionadas son incorrectas. Por favor, verifica tu usuario y contraseña."
    }


@router.post("/login")
def login(credenciales: Credenciales = Body(...)):
    return autenticar_usuario(credenciales)
