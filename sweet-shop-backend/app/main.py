from fastapi import FastAPI
from app.api import auth, sweets
from app.db.init_db import init_db

app = FastAPI(title="Sweet Shop Management System")

init_db()


@app.get("/")
def root():
    return {"message": "Sweet Shop Backend is running"}


app.include_router(auth.router)
app.include_router(sweets.router)
