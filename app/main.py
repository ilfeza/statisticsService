from fastapi import FastAPI
from app.database import Base, engine
from app.endpoints.devices import router as devices_router


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(devices_router, prefix="/devices")

