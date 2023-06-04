from fastapi import APIRouter, Header

from diagrams.schemas import NameDescriptionSchema
from utils import async_post, async_put
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
