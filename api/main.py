from fastapi import FastAPI, Depends, HTTPException, Request
from cryptography.fernet import Fernet
from itsdangerous import TimedSerializer as Serializer
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret_key")
ORIGIN = os.environ.get("APP_ORIGIN", "http://localhost:8000")

serializer = Serializer(SECRET_KEY)

key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.post("/generate_key/")
def generate_key():
    return {"key": key.decode()}

@app.post("/encrypt_data/")
def encrypt_data(data: str):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return {"encrypted_data": encrypted_data.decode()}

@app.post("/decrypt_data/")
def decrypt_data(data: str):
    decrypted_data = cipher_suite.decrypt(data.encode())
    return {"decrypted_data": decrypted_data.decode()}

@app.middleware("http")
async def check_origin(request: Request, call_next):
    if "origin" in request.headers and request.headers["origin"] != ORIGIN:
        raise HTTPException(status_code=400, detail="Cross-origin request detected!")
    response = await call_next(request)
    return response

