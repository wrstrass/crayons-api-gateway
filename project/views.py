from fastapi import APIRouter, Header

from project.schemas import NameSchema, UserAndGroupSchema, ProjectSchema, PermissionSet
from utils import async_get, async_post, async_put
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

@router.get("/{project_name}/")
async def get_project(project_name: str, access_token: str | None = Header(default=None)) -> ProjectSchema:
    res = await async_get(
        f"{projects_url}/{project_name}/",
        headers={} if access_token is None else {
            "Access-Token": access_token,
        },
    )
    return res.to_response()

@router.put("/{project_name}/user")
async def project_add_user(project_name: str, data: UserAndGroupSchema, access_token: str = Header()) -> ProjectSchema:
    res = await async_put(
        f"{projects_url}/{project_name}/user",
        data.dict(),
        headers={
            "Access-Token": access_token,
        },
    )
    return res.to_response()

@router.put("/{project_name}/permissions")
async def project_permissions(project_name: str, permissions: PermissionSet, access_token: str = Header()) -> ProjectSchema:
    res = await async_put(
        f"{projects_url}/{project_name}/permissions",
        permissions.dict(),
        headers={
            "Access-Token": access_token,
        },
    )
    return res.to_response()
