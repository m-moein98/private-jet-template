from fastapi import FastAPI

from the_app.router import router as theapp_router


app = FastAPI()

app.include_router(theapp_router, prefix="/theapp", tags=["theapp"])
