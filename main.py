from fastapi import FastAPI
from web import routes

app = FastAPI()

app.include_router(routes.router)
