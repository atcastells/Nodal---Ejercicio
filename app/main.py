from fastapi import FastAPI
from app.core.config import Settings

settings = Settings()
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Nodal API", "settings": settings.model_dump()}

print(f"Settings loaded: {settings}")
