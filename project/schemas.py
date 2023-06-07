from enum import StrEnum, auto
from pydantic import BaseModel


class NameSchema(BaseModel):
    name: str

class UserAndGroupSchema(BaseModel):
    user: int
    group: str


class Permission(StrEnum):
    FORBID = auto()
    VIEW = auto()
    EDIT = auto()
    FULL = auto()

class PermissionSet(BaseModel):
    owner: Permission = Permission.FULL
    dev: Permission = Permission.EDIT
    user: Permission = Permission.VIEW
    etc: Permission = Permission.FORBID


class Members(BaseModel):
    owners: list[int] = []
    devs: list[int] = []
    users: list[int] = []


class ProjectSchema(BaseModel):
    name: str
    permissions: PermissionSet
    members: Members
    diagrams: list[str]

class ProjectOverview(BaseModel):
    name: str
    group: str
    permission: Permission
    diagrams: int
