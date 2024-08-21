from fastapi import FastAPI

from routers.consumo import router as consumo_router
from routers.dispositivo import router as dispositivo_router
from routers.comodo import router as comodo_router
from routers.residencia import router as residencia_router

from config.database import startup_db, shutdown_db

app = FastAPI()

app.add_event_handler("startup", startup_db)
app.add_event_handler("shutdown", shutdown_db)

app.include_router(residencia_router)
app.include_router(comodo_router)
app.include_router(dispositivo_router)
app.include_router(consumo_router)
