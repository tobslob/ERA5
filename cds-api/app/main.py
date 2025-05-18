from fastapi import FastAPI
from app.routes import router as climate_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ERA5 Climate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(climate_router, prefix="/api/climate")
