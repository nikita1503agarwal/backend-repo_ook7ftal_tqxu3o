from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Gokul Portfolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running", "app": "Gokul Portfolio API"}

@app.get("/test")
def test():
    # Simple diagnostics endpoint
    return {
        "backend": "FastAPI",
        "database": "Not used for this demo",
        "database_url": "N/A",
        "database_name": "N/A",
        "connection_status": "OK",
        "collections": []
    }
