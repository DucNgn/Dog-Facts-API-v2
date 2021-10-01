import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from v1.routers.facts import v1_router

from config import NAME, HOST, PORT, VERSION


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=NAME,
        version=VERSION,
        description="A public API service to retrive cool dog facts",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def add_test_endpoint(app: FastAPI):
    @app.get("/")
    async def home():
        return {
            "message": "Welcome to Dog Facts API!. Go to endpoint /docs to access the interactive documentation."
        }


def create_app():
    """
    Create the FastAPI instance and attach routers.
    """
    app = FastAPI()
    app.openapi = custom_openapi
    add_test_endpoint(app)
    app.include_router(v1_router)

    return app


if __name__ == "__main__":
    app = create_app()
    uvicorn.run(app, host=HOST, port=PORT)
