from fastapi import FastAPI
from utils import async_post


PREFIX = "/api/v1"

MICROSERVICES = {
    "auth": "http://auth:8001/api/v1/auth",
}


app = FastAPI(
    docs_url=f"{PREFIX}/docs/",
    redoc_url=f"{PREFIX}/redoc/",
    openapi_url=f"{PREFIX}/openapi.json",
)


@app.get(f"{PREFIX}/register/")
async def register():
    response = await async_post(f"{MICROSERVICES['auth']}/register/")
    return response
