from fastapi import APIRouter, HTTPException, status
from typing import Dict
from ..models import Credentials

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

    # Return a success message if authentication is successful
    return {"message": "Authentication successful"}


@router.post("/login")
def login(credentials: Credentials):
    # Authenticate the user and return the response
    return authenticate_user(credentials)
