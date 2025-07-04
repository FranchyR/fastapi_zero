from fastapi import FastAPI

from fastapi_zero.routers import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
