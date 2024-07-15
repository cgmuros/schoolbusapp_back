from fastapi import APIRouter, Depends, HTTPException
from ..auth import verify_token, security

router = APIRouter()


@router.get("/protected")
def protected_endpoint(username: str = Depends(verify_token)):
    # This endpoint can only be accessed with a valid JWT
    return {"message": f"Hello, {username}!"}


@router.get("/unprotected")
def unprotected_endpoint():
    # This endpoint can be accessed without authentication
    return {"message": "This is an unprotected endpoint."}

