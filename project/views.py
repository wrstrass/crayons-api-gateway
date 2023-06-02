from fastapi import APIRouter, Header

from project.schemas import NameSchema, ProjectSchema
from utils import async_post
from const import MICROSERVICES


projects_url = MICROSERVICES["projects"]

router = APIRouter(
    prefix="/projects",
    tags=["projects",],
)


@router.post("/")
async def new_project(name: NameSchema, access_token: str = Header()) -> ProjectSchema:
    res = await async_post(
        f"{projects_url}/",
        name.dict(),
        headers={
            "Access-Token": access_token,
        },
    )
    return res.to_response()

# MOCK DATA
@router.get("/")
async def get_projects(access_token: str = Header()) -> list[ProjectSchema]:
    return [
        {
            "name": "TestProject1",
            "permission": "view",
            "group": "user",
        },
        {
            "name": "TestProject2",
            "permission": "edit",
            "group": "dev",
        },
    ]
