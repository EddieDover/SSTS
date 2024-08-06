from fastapi import FastAPI

def bootstrap() -> FastAPI:
    app = FastAPI()
    return app