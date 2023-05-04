from pydantic import BaseModel


class NameSchema(BaseModel):
    name: str


class ProjectOverview(BaseModel):
    name: str
    permission: str
    group: str
