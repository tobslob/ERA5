from fastapi import FastAPI
from app.routes import router as climate_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ERA5 Climate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(climate_router, prefix="/api/climate")
