from fastapi import FastAPI, APIRouter
from const import PREFIX
import auth


app = FastAPI(
    docs_url=f"{PREFIX}/docs/",
    redoc_url=f"{PREFIX}/redoc/",
    openapi_url=f"{PREFIX}/openapi.json",
)

router = APIRouter(prefix=PREFIX)
router.include_router(auth.router)

app.include_router(router)
