from fastapi import FastAPI
from .routes import auth, example

app = FastAPI()

# Include the authentication routes
app.include_router(auth.router)

# Include the protected routes
app.include_router(example.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
