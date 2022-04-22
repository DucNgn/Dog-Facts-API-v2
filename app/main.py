import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.v1.routers.facts import v1_router

from config import NAME, HOST, PORT, VERSION, HOMEPAGE

origins = ["*"]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=NAME,
        version=VERSION,
        description=f"A public API service to retrieve cool dog facts. Homepage: {HOMEPAGE}",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def add_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def add_test_endpoint(app: FastAPI):
    @app.get("/")
    async def home():
        return {
            "message": "Welcome to Dog Facts API!. Go to endpoint /docs to access the interactive documentation."
        }


def add_exception_handler(app: FastAPI):
    @app.exception_handler(ValueError)
    @app.exception_handler(RequestValidationError)
    async def value_error_exception_handler(request: Request, exc):
        """
        Custom Exception Handler
        """
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={"message": str(exc)}
        )


app = FastAPI()
app.openapi = custom_openapi
add_test_endpoint(app)
add_middlewares(app)
add_exception_handler(app)
app.include_router(v1_router)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
