from fastapi import APIRouter

from const import MICROSERVICES
from utils import async_post
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
