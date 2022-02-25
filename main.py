from the_app.router import router as theapp_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(theapp_router, prefix="/theapp", tags=["theapp"])
