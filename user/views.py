from fastapi import APIRouter

from user.schemas import UserSearchSchema, UserSchema
from utils import async_get, async_post
from const import MICROSERVICES


user_url = MICROSERVICES["user"]

router = APIRouter(
    prefix="/user",
    tags=["user",],
)


@router.post("/search")
async def search(search_schema: UserSearchSchema) -> list[UserSchema]:
    res = await async_post(f"{user_url}/search", search_schema.dict())
    return res.to_response()

@router.get("/{user_id}")
async def get_by_id(user_id: int) -> str:
    res = await async_get(f"{user_url}/{user_id}")
    return res.to_response()
