from fastapi import APIRouter, Header

from diagrams.schemas import NameDescriptionSchema
from utils import async_get, async_post, async_put
from const import MICROSERVICES


diagrams_url = MICROSERVICES["diagrams"]
projects_url = MICROSERVICES["projects"]

router = APIRouter(
    prefix="/diagrams",
    tags=["diagrams",],
)


@router.post("/{project_name}/")
async def new_diagram(project_name: str, data: NameDescriptionSchema, access_token: str = Header()):
    res = await async_post(
        f"{diagrams_url}/",
        data.dict(),
    )
    await async_put(
        f"{projects_url}/{project_name}/{res.body['id']}",
        headers={
            "Access-Token": access_token,
        },
    )
    return res.to_response()

@router.get("/{diagram_oid}/")
async def get_diagram(diagram_oid: str, access_token: str = Header()):
    res = await async_get(f"{diagrams_url}/{diagram_oid}/")
    return res.to_response()

@router.get("/{diagram_oid}/shapes")
async def get_diagram_shapes(diagram_oid: str, access_token: str = Header()):
    res = await async_get(f"{diagrams_url}/{diagram_oid}/shapes")
    return res.to_response()

@router.get("/{diagram_oid}/access")
async def get_diagram_access(diagram_oid: str, access_token: str = Header()):
    res = await async_get(
        f"{projects_url}/{diagram_oid}/access",
        headers={
            "Access-Token": access_token,
        },
    )
    return res.to_response()
