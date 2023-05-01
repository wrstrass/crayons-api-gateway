from pydantic import BaseModel, constr
from user import UserSchema


class AuthSchema(BaseModel):
    username: constr(min_length=5, strict=True)
    password: constr(min_length=8, strict=True)
