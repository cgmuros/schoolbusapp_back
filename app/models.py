from pydantic import BaseModel


class Credentials(BaseModel):
    # User's email or username
    username: str
    # User's password
    password: str
