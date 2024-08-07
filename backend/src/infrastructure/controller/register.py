from fastapi import APIRouter
from fastapi.responses import JSONResponse

class RegisterController:
    def __init__(self) -> None:
        self.router = APIRouter(
            prefix= "/register",
            tags= ["User Auth"]
        )
        self.router.add_api_route("", self.register_user, methods= ["POST"], status_code= 200)

    async def register_user(self) -> JSONResponse:
        return JSONResponse(status_code= 200, content= {"message": string_no})
    