from fastapi import FastAPI
from .routes import auth

app = FastAPI()

# Include the authentication routes
app.include_router(auth.router)

if __name__ == "__main__":
    # Run the application if this file is executed directly
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
