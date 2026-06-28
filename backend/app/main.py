from fastapi import FastAPI

from app.api.projects import router as project_router

app = FastAPI(
    title="Claudable Cloud Backend",
    version="1.0.0"
)

app.include_router(project_router)


@app.get("/")
def home():
    return {
        "message": "Claudable Cloud Backend is Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }