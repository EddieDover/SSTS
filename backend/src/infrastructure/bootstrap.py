from fastapi import FastAPI
from kink import di

from infrastructure.controller.register import RegisterController

def bootstrap_di() -> None:
    di[RegisterController] = RegisterController()

def bootstrap_api(app: FastAPI) -> None:
    app.include_router(di[RegisterController].router)

def bootstrap() -> FastAPI:
    bootstrap_di()
    app = FastAPI()
    bootstrap_api(app)
    return app
