from fastapi import FastAPI
from kink import di
from sqlmodel import SQLModel, Field, create_engine
from sqlalchemy import Engine, create_engine

from infrastructure.controller.register import RegisterController

def bootstrap_di() -> None:
    di[Engine] = bootstrap_db()
    di[RegisterController] = RegisterController()

def bootstrap_api(app: FastAPI) -> None:
    app.include_router(di[RegisterController].router)

def bootstrap_db() -> Engine:
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///E:\\Alex\\Computer Science\\Repository\\{sqlite_file_name}"
    engine = create_engine(sqlite_url)
    SQLModel.metadata.create_all(engine)
    return engine

def bootstrap() -> FastAPI:
    bootstrap_di()
    app = FastAPI()
    bootstrap_api(app)
    return app
