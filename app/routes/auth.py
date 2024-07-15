from fastapi import APIRouter, HTTPException, status
from typing import Dict
from ..models import Credentials
from ..auth import create_access_token

router = APIRouter()

# Simulated user database
users = {
    "user1": {"name": "cgmuros@gmail.com", "password": "alfa1414"},
    "user2": {"name": "ilsesilva@gmail.com", "password": "alfa1414"},
}


def authenticate_user(credentials: Credentials) -> Dict[str, str]:
    # Find the user in the database
    user_data = next((data for data in users.values() if data["name"] == credentials.username), None)

    # If user not found or password is incorrect, raise an exception
    if not user_data or user_data["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create and return an access token
    access_token = create_access_token(credentials.username)
    return {"access_token": access_token}


@router.post("/login")
def login(credentials: Credentials):
    # Authenticate the user and return the access token
    return authenticate_user(credentials)
