from fastapi import APIRouter, Header

from const import MICROSERVICES
from utils import async_get, async_post
from auth.schemas import AuthSchema


auth_url = MICROSERVICES["auth"]

router = APIRouter(
    prefix="/auth",
    tags=["auth",],
)


@router.post("/register")
async def register(auth: AuthSchema):
    res = await async_post(f"{auth_url}/register", auth.dict())
    return res.to_response()

@router.post("/login")
async def login(auth: AuthSchema):
    res = await async_post(f"{auth_url}/login", auth.dict())
    return res.to_response()

@router.get("/tokens")
async def tokens(refresh_token: str = Header()):
    res = await async_get(f"{auth_url}/tokens", headers={
        "Refresh-Token": refresh_token,
    })
    return res.to_response()
