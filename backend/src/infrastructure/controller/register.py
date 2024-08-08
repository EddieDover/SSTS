from fastapi import APIRouter
from fastapi.responses import JSONResponse
from kink import inject
from sqlalchemy import Engine
from infrastructure.entity.student import Student
from infrastructure.db.session_manager import get_session

@inject
class RegisterController:
    def __init__(self, engine: Engine) -> None:
        self.db = engine
        self.router = APIRouter(
            prefix= "/register",
            tags= ["User Auth"]
        )
        self.router.add_api_route("", self.register_user, methods= ["POST"], status_code= 200)

    async def register_user(self) -> JSONResponse:
        user = Student(email= "john@example.com", password= "password12", surname="smith", name="john")
        with get_session(self.db) as session:
            session.add(user)
            session.commit()
        return JSONResponse(status_code= 200, content= {"message": "User successfully registered"})

    