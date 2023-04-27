from fastapi import APIRouter, Header

from utils import async_get, async_post
from auth.schemas import AuthSchema, UserSchema
from const import MICROSERVICES
from responses import EMPTY_RESPONSE, EMPTY_WITH_TOKENS_COOKIES, DETAIL_INFO


auth_url = MICROSERVICES["auth"]

router = APIRouter(
    prefix="/auth",
    tags=["auth",],
)


@router.post("/register", responses={
    200: EMPTY_RESPONSE,
    403: DETAIL_INFO,
})
async def register(auth: AuthSchema):
    res = await async_post(f"{auth_url}/register", auth.dict())
    return res.to_response()


@router.post("/login", responses={
    200: EMPTY_WITH_TOKENS_COOKIES,
    403: DETAIL_INFO,
    404: EMPTY_RESPONSE,
})
async def login(auth: AuthSchema):
    res = await async_post(f"{auth_url}/login", auth.dict())
    return res.to_response()


@router.get("/tokens", responses={
    200: EMPTY_WITH_TOKENS_COOKIES,
    401: DETAIL_INFO,
})
async def tokens(refresh_token: str = Header()):
    res = await async_get(f"{auth_url}/tokens", headers={
        "Refresh-Token": refresh_token,
    })
    return res.to_response()


@router.get("/me", responses={
    200: {
        "model": UserSchema,
    },
    401: DETAIL_INFO,
})
async def me(access_token: str = Header()):
    res = await async_get(f"{auth_url}/me", headers={
        "Access-Token": access_token,
    })
    return res.to_response()
