from pydantic import BaseModel, constr


class AuthSchema(BaseModel):
    login: constr(min_length=5, strict=True)
    password: constr(min_length=8, strict=True)
